"""Subscribe to FastComments live changes over WebSocket.

This mirrors the Java pubsub ``LiveEventSubscriber``: it opens a WebSocket to the
FastComments live server, hands each parsed :class:`LiveEvent` to a callback, fetches
any missed events from the event-log REST endpoint on (re)connect, and transparently
reconnects with jitter until the caller closes the subscription.
"""

import json
import logging
import random
import threading
import time
from typing import Callable, Dict, List, Optional
from urllib.parse import urlencode

from client import ApiClient, Configuration, PublicApi
from client.models.live_event import LiveEvent
from client.models.live_event_type import LiveEventType

from .subscribe_to_changes_result import SubscribeToChangesResult

try:
    import websocket  # provided by the "websocket-client" package
except ImportError:  # pragma: no cover - surfaced lazily with a helpful message
    websocket = None

logger = logging.getLogger("fastcomments.pubsub")

RECONNECT_INTERVAL_BASE_SECONDS = 4.0
DEFAULT_PING_INTERVAL_SECONDS = 25
TESTING_PING_INTERVAL_SECONDS = 5
FETCH_EVENT_LOG_DEBOUNCE_SECONDS = 2.0

# Callback signatures:
#   handle_live_event(event: LiveEvent) -> None
#   can_see_comments(comment_ids: List[str]) -> Dict[str, str]   (returns blocked-id map)
#   on_connection_status_change(is_connected: bool, last_live_event_time: Optional[int]) -> None
HandleLiveEventCallback = Callable[[LiveEvent], None]
CanSeeCommentsCallback = Callable[[List[str]], Dict[str, str]]
ConnectionStatusChangeCallback = Callable[[bool, Optional[int]], None]


def _now_ms() -> int:
    return int(time.time() * 1000)


class LiveEventSubscriber:
    """Manages a live WebSocket subscription to FastComments events."""

    def __init__(self, ping_interval_seconds: int = DEFAULT_PING_INTERVAL_SECONDS) -> None:
        self._ping_interval_seconds = ping_interval_seconds
        self.on_connection_status_change: Optional[ConnectionStatusChangeCallback] = None

    @classmethod
    def create_testing(cls) -> "LiveEventSubscriber":
        """Create a subscriber with a short ping interval, useful for aggressive NAT environments."""
        return cls(ping_interval_seconds=TESTING_PING_INTERVAL_SECONDS)

    @staticmethod
    def _extract_comment_id_from_event(event: LiveEvent) -> Optional[str]:
        if event.type == LiveEventType.NEW_MINUS_COMMENT and event.comment is not None:
            return event.comment.id
        return None

    def subscribe_to_changes(
        self,
        tenant_id_ws: str,
        url_id: str,
        url_id_ws: str,
        user_id_ws: str,
        handle_live_event: HandleLiveEventCallback,
        can_see_comments: Optional[CanSeeCommentsCallback] = None,
        on_connection_status_change: Optional[ConnectionStatusChangeCallback] = None,
        region: Optional[str] = None,
        disable_live_commenting: bool = False,
        api_host: str = "https://fastcomments.com",
        api_client: Optional[ApiClient] = None,
    ) -> Optional[SubscribeToChangesResult]:
        """Open a live subscription and return a handle for closing it.

        :param tenant_id_ws: The tenant id, sanitized for the websocket server.
        :param url_id: The url id that events are tied to (used when fetching the event log).
        :param url_id_ws: The url id, sanitized for the websocket server.
        :param user_id_ws: The user's "presence id".
        :param handle_live_event: Called with each :class:`LiveEvent` that is received.
        :param can_see_comments: Optional callback that receives a list of comment ids and
            returns a dict whose keys are the ids the user is NOT allowed to see. Events for
            blocked comment ids are dropped before ``handle_live_event`` is called.
        :param on_connection_status_change: Optional callback invoked with
            ``(is_connected, last_live_event_time)`` whenever the connection opens or drops.
        :param region: Set to ``"eu"`` to use the EU websocket host.
        :param disable_live_commenting: When ``True``, no connection is opened and ``None`` is returned.
        :param api_host: REST host used to fetch missed events from the event log.
        :param api_client: Optional pre-configured :class:`client.ApiClient` for the event-log
            requests. When omitted one is built from ``api_host``.
        :return: A :class:`SubscribeToChangesResult`, or ``None`` if live commenting is disabled
            or the ``websocket-client`` dependency is not installed.
        """
        if disable_live_commenting:
            return None

        if websocket is None:
            logger.error(
                "FastComments: the 'websocket-client' package is required for live subscriptions. "
                "Install it with: pip install \"fastcomments[pubsub]\""
            )
            return None

        if on_connection_status_change is not None:
            self.on_connection_status_change = on_connection_status_change

        if api_client is None:
            # Default the event-log REST host from the region so the "fetch missed events"
            # fallback queries EU infra for EU tenants instead of silently hitting US.
            if api_host == "https://fastcomments.com" and region == "eu":
                api_host = "https://eu.fastcomments.com"
            api_client = ApiClient(Configuration(host=api_host))
        public_api = PublicApi(api_client)

        # Per-subscription state shared across reconnects.
        state = {
            "last_event_time": _now_ms(),
            "intentionally_closed": False,
            "app": None,  # type: Optional[websocket.WebSocketApp]
            "fetch_timer": None,  # type: Optional[threading.Timer]
            "reconnect_timer": None,  # type: Optional[threading.Timer]
        }

        ws_host = "wss://ws-eu.fastcomments.com" if region == "eu" else "wss://ws.fastcomments.com"
        query = urlencode({"urlId": url_id_ws, "userIdWS": user_id_ws, "tenantIdWS": tenant_id_ws})
        ws_url = f"{ws_host}/sub?{query}"

        def process_events(events: List[LiveEvent]) -> None:
            if not events:
                return

            blocked_map: Optional[Dict[str, str]] = None
            if can_see_comments is not None:
                ids = [
                    comment_id
                    for comment_id in (self._extract_comment_id_from_event(event) for event in events)
                    if comment_id is not None
                ]
                if ids:
                    try:
                        blocked_map = can_see_comments(ids)
                    except Exception as exc:  # noqa: BLE001 - never let a user callback break the stream
                        logger.error("FastComments: can_see_comments callback failed: %s", exc)
                        blocked_map = None

            for event in events:
                try:
                    if event.timestamp is not None:
                        state["last_event_time"] = max(state["last_event_time"], event.timestamp)
                    comment_id = self._extract_comment_id_from_event(event)
                    if blocked_map is None or comment_id not in blocked_map:
                        handle_live_event(event)
                except Exception as exc:  # noqa: BLE001
                    logger.error("FastComments: error processing event: %s", exc)

        def fetch_event_log(start_time: int, end_time: int) -> None:
            if state["intentionally_closed"]:
                return

            def run() -> None:
                try:
                    response = public_api.get_event_log(
                        tenant_id_ws, url_id, user_id_ws, start_time, end_time
                    )
                    parsed: List[LiveEvent] = []
                    for entry in response.events or []:
                        if entry.data:
                            try:
                                event = LiveEvent.from_json(entry.data)
                                if event is not None:
                                    parsed.append(event)
                            except Exception as exc:  # noqa: BLE001
                                logger.error("FastComments: error parsing event data: %s", exc)
                    process_events(parsed)
                except Exception as exc:  # noqa: BLE001
                    logger.error("FastComments: fetch_event_log failure: %s", exc)

            # Debounce so a burst of reconnect attempts doesn't hammer the event-log endpoint.
            if state["fetch_timer"] is not None:
                state["fetch_timer"].cancel()
            timer = threading.Timer(FETCH_EVENT_LOG_DEBOUNCE_SECONDS, run)
            timer.daemon = True
            state["fetch_timer"] = timer
            timer.start()

        def connect() -> None:
            if state["intentionally_closed"]:
                return

            def on_open(_app) -> None:
                if state["intentionally_closed"]:
                    _app.close()
                    return
                if state["last_event_time"] > 0:
                    fetch_event_log(state["last_event_time"], _now_ms())
                if self.on_connection_status_change is not None:
                    self.on_connection_status_change(True, state["last_event_time"])

            def on_message(_app, message) -> None:
                if state["intentionally_closed"]:
                    return
                try:
                    event = LiveEvent.from_json(message)
                    if event is None:
                        return
                    if event.timestamp is not None:
                        # ts (present on presence-only updates) is intentionally not tracked,
                        # since those events are not stored in the log.
                        state["last_event_time"] = max(state["last_event_time"], event.timestamp)
                    process_events([event])
                except Exception as exc:  # noqa: BLE001
                    logger.error("FastComments: error processing WebSocket message: %s", exc)

            def on_error(_app, error) -> None:
                logger.error("FastComments: WebSocket error: %s", error)
                if state["last_event_time"] > 0:
                    fetch_event_log(state["last_event_time"], _now_ms())

            def on_close(_app, _status_code, _msg) -> None:
                if state["fetch_timer"] is not None:
                    state["fetch_timer"].cancel()
                    state["fetch_timer"] = None

                if state["last_event_time"] <= 0:
                    state["last_event_time"] = _now_ms()

                if state["intentionally_closed"]:
                    return

                if self.on_connection_status_change is not None:
                    self.on_connection_status_change(False, state["last_event_time"])

                reconnect_delay = RECONNECT_INTERVAL_BASE_SECONDS * random.random()
                reconnect_timer = threading.Timer(reconnect_delay, connect)
                reconnect_timer.daemon = True
                state["reconnect_timer"] = reconnect_timer
                reconnect_timer.start()

            app = websocket.WebSocketApp(
                ws_url,
                on_open=on_open,
                on_message=on_message,
                on_error=on_error,
                on_close=on_close,
            )
            state["app"] = app

            def run_forever() -> None:
                # Protocol-level ping keeps NATs (emulators, silly networks, etc) alive.
                app.run_forever(ping_interval=self._ping_interval_seconds)

            thread = threading.Thread(target=run_forever, name="fastcomments-live", daemon=True)
            thread.start()

        connect()

        def close() -> None:
            state["intentionally_closed"] = True
            if state["reconnect_timer"] is not None:
                state["reconnect_timer"].cancel()
            if state["fetch_timer"] is not None:
                state["fetch_timer"].cancel()
            if state["app"] is not None:
                try:
                    state["app"].close()
                except Exception as exc:  # noqa: BLE001
                    logger.error("FastComments: error closing WebSocket: %s", exc)

        return SubscribeToChangesResult(close)
