"""Unit tests for the live pubsub subscriber (no real network)."""

import json
from unittest.mock import MagicMock, patch

import pytest

from client.models.event_log_entry import EventLogEntry
from client.models.get_event_log_response import GetEventLogResponse
from pubsub import LiveEventSubscriber, SubscribeToChangesResult


def _new_comment_event(comment_id: str, timestamp: int = 1000) -> dict:
    """A minimal 'new-comment' LiveEvent payload as sent by the live server."""
    return {
        "type": "new-comment",
        "timestamp": timestamp,
        "comment": {
            "_id": comment_id,
            "tenantId": "tenant-1",
            "urlId": "url-1",
            "commenterName": "Test User",
            "commentHTML": "<p>hello</p>",
            "comment": "hello",
            "verified": True,
            "url": "https://example.com/article",
            "approved": True,
            "date": "2024-01-01T00:00:00Z",
        },
    }


class FakeWebSocketApp:
    """Captures the handlers passed by the subscriber so tests can drive them synchronously."""

    last_instance = None

    def __init__(self, url, on_open=None, on_message=None, on_error=None, on_close=None):
        self.url = url
        self.on_open = on_open
        self.on_message = on_message
        self.on_error = on_error
        self.on_close = on_close
        self.closed = False
        FakeWebSocketApp.last_instance = self

    def run_forever(self, ping_interval=None):
        # Do not block; a real run loop would sit here until close.
        self.ping_interval = ping_interval

    def close(self):
        self.closed = True


@pytest.fixture(autouse=True)
def fake_websocket():
    with patch("pubsub.live_event_subscriber.websocket") as ws_module:
        ws_module.WebSocketApp = FakeWebSocketApp
        FakeWebSocketApp.last_instance = None
        yield ws_module


def _make_subscriber():
    """A subscriber whose event-log fetch is a no-op unless a test overrides it."""
    return LiveEventSubscriber()


def test_disable_live_commenting_returns_none():
    result = LiveEventSubscriber().subscribe_to_changes(
        "tenant-1", "url-1", "url-1", "user-ws-1", lambda e: None, disable_live_commenting=True
    )
    assert result is None


def test_returns_result_and_builds_ws_url():
    result = _make_subscriber().subscribe_to_changes(
        "tenant-1", "url-1", "url-1-ws", "user-ws-1", lambda e: None
    )
    assert isinstance(result, SubscribeToChangesResult)
    app = FakeWebSocketApp.last_instance
    assert app is not None
    assert app.url.startswith("wss://ws.fastcomments.com/sub?")
    assert "urlId=url-1-ws" in app.url
    assert "userIdWS=user-ws-1" in app.url
    assert "tenantIdWS=tenant-1" in app.url
    result.close()


def test_eu_region_uses_eu_host():
    _make_subscriber().subscribe_to_changes(
        "tenant-1", "url-1", "url-1", "user-ws-1", lambda e: None, region="eu"
    )
    assert FakeWebSocketApp.last_instance.url.startswith("wss://ws-eu.fastcomments.com/sub?")


def test_on_message_dispatches_parsed_live_event():
    received = []
    _make_subscriber().subscribe_to_changes(
        "tenant-1", "url-1", "url-1", "user-ws-1", received.append
    )
    app = FakeWebSocketApp.last_instance
    app.on_message(app, json.dumps(_new_comment_event("comment-1")))
    assert len(received) == 1
    assert received[0].type.value == "new-comment"
    assert received[0].comment.id == "comment-1"


def test_can_see_comments_blocks_events():
    received = []
    _make_subscriber().subscribe_to_changes(
        "tenant-1",
        "url-1",
        "url-1",
        "user-ws-1",
        received.append,
        can_see_comments=lambda ids: {"comment-blocked": "1"},
    )
    app = FakeWebSocketApp.last_instance
    app.on_message(app, json.dumps(_new_comment_event("comment-blocked")))
    app.on_message(app, json.dumps(_new_comment_event("comment-visible")))
    assert [e.comment.id for e in received] == ["comment-visible"]


def test_connection_status_callback_fires_on_open():
    statuses = []
    _make_subscriber().subscribe_to_changes(
        "tenant-1",
        "url-1",
        "url-1",
        "user-ws-1",
        lambda e: None,
        on_connection_status_change=lambda connected, ts: statuses.append(connected),
    )
    app = FakeWebSocketApp.last_instance
    app.on_open(app)
    assert statuses == [True]


def test_close_marks_intentional_and_prevents_reconnect():
    result = _make_subscriber().subscribe_to_changes(
        "tenant-1", "url-1", "url-1", "user-ws-1", lambda e: None
    )
    app = FakeWebSocketApp.last_instance
    result.close()
    assert app.closed is True
    # An intentional close must not schedule a reconnect (no new app instance).
    app.on_close(app, 1000, "bye")
    assert FakeWebSocketApp.last_instance is app


def test_eu_region_event_log_uses_eu_host():
    with patch("pubsub.live_event_subscriber.ApiClient") as ApiClientMock, patch(
        "pubsub.live_event_subscriber.Configuration"
    ) as ConfigurationMock:
        _make_subscriber().subscribe_to_changes(
            "tenant-1", "url-1", "url-1", "user-ws-1", lambda e: None, region="eu"
        )
        ConfigurationMock.assert_called_once_with(host="https://eu.fastcomments.com")


def test_us_region_event_log_uses_us_host():
    with patch("pubsub.live_event_subscriber.ApiClient"), patch(
        "pubsub.live_event_subscriber.Configuration"
    ) as ConfigurationMock:
        _make_subscriber().subscribe_to_changes(
            "tenant-1", "url-1", "url-1", "user-ws-1", lambda e: None
        )
        ConfigurationMock.assert_called_once_with(host="https://fastcomments.com")


def test_explicit_api_host_overrides_region_default():
    with patch("pubsub.live_event_subscriber.ApiClient"), patch(
        "pubsub.live_event_subscriber.Configuration"
    ) as ConfigurationMock:
        _make_subscriber().subscribe_to_changes(
            "tenant-1",
            "url-1",
            "url-1",
            "user-ws-1",
            lambda e: None,
            region="eu",
            api_host="https://my-proxy.example.com",
        )
        ConfigurationMock.assert_called_once_with(host="https://my-proxy.example.com")


def test_open_fetches_missed_events_from_event_log():
    received = []
    subscriber = _make_subscriber()

    missed = GetEventLogResponse(
        events=[
            EventLogEntry(
                _id="e1",
                createdAt="2024-01-01T00:00:00Z",
                tenantId="tenant-1",
                urlId="url-1",
                broadcastId="b1",
                data=json.dumps(_new_comment_event("missed-comment", timestamp=999)),
            )
        ],
        status="success",
    )

    with patch("pubsub.live_event_subscriber.PublicApi") as PublicApiMock, patch(
        "pubsub.live_event_subscriber.FETCH_EVENT_LOG_DEBOUNCE_SECONDS", 0.0
    ):
        instance = PublicApiMock.return_value
        instance.get_event_log.return_value = missed

        result = subscriber.subscribe_to_changes(
            "tenant-1", "url-1", "url-1", "user-ws-1", received.append
        )
        app = FakeWebSocketApp.last_instance
        app.on_open(app)
        # Debounced fetch runs on a Timer thread; give it a moment.
        import time

        deadline = time.time() + 2
        while not received and time.time() < deadline:
            time.sleep(0.02)

    result.close()
    assert instance.get_event_log.called
    assert [e.comment.id for e in received] == ["missed-comment"]
