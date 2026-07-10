"""Result of subscribing to changes."""

from typing import Callable, Optional


class SubscribeToChangesResult:
    """Handle returned by ``subscribe_to_changes``; call ``close()`` to stop the subscription."""

    def __init__(self, close_action: Optional[Callable[[], None]] = None) -> None:
        self._close_action = close_action

    def close(self) -> None:
        """Intentionally close the connection and stop reconnecting."""
        if self._close_action is not None:
            self._close_action()
