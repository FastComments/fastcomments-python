import json


class SecureSSOPayload:
    """A signed Secure SSO payload in the FastComments wire format.

    On the wire the keys are camelCase (`userDataJSONBase64`,
    `verificationHash`, `timestamp`) with `timestamp` in epoch milliseconds;
    `loginURL`/`logoutURL` are included only when set.
    """

    def __init__(
        self,
        user_data_json_base64: str,
        verification_hash: str,
        timestamp: int,
        login_url: str = None,
        logout_url: str = None,
    ):
        self.user_data_json_base64 = user_data_json_base64
        self.verification_hash = verification_hash
        self.timestamp = timestamp
        self.login_url = login_url
        self.logout_url = logout_url

    def to_widget_dict(self) -> dict:
        """The object the widget expects at `config.sso`."""
        result = {
            "userDataJSONBase64": self.user_data_json_base64,
            "verificationHash": self.verification_hash,
            "timestamp": self.timestamp,
        }
        if self.login_url is not None:
            result["loginURL"] = self.login_url
        if self.logout_url is not None:
            result["logoutURL"] = self.logout_url
        return result

    def toJSON(self) -> str:
        return json.dumps(self.to_widget_dict(), separators=(",", ":"))
