import json


class SimpleSSOUserData:
    """User identity for Simple (unsigned) SSO.

    The widget's `simpleSSO` object is keyed on `username`; unset optionals are
    omitted. This is less secure than Secure SSO and carries no signature.
    """

    _FIELDS = (
        ("username", "username"),
        ("email", "email"),
        ("avatar", "avatar"),
        ("website_url", "websiteUrl"),
        ("display_name", "displayName"),
    )

    def __init__(
        self,
        username=None,
        email=None,
        avatar=None,
        website_url=None,
        display_name=None,
        **extra,
    ):
        self.username = username
        self.email = email
        self.avatar = avatar
        self.website_url = website_url
        self.display_name = display_name
        self.extra = {k: v for k, v in extra.items() if v is not None}

    def to_dict(self) -> dict:
        result = {}
        for attr, wire_key in self._FIELDS:
            value = getattr(self, attr)
            if value is not None:
                result[wire_key] = value
        result.update(self.extra)
        return result

    def toJSON(self) -> str:
        return json.dumps(self.to_dict(), separators=(",", ":"))
