import json
import base64


class SecureSSOUserData:
    """User identity for Secure SSO.

    Serializes to the exact JSON the FastComments server validates: keyed on
    `id` (required), compact, camelCase optional fields, with unset optionals
    omitted. `id` is always stringified.
    """

    # snake_case constructor arg -> camelCase wire key, in serialization order.
    _FIELDS = (
        ("id", "id"),
        ("email", "email"),
        ("username", "username"),
        ("avatar", "avatar"),
        ("display_name", "displayName"),
        ("display_label", "displayLabel"),
        ("website_url", "websiteUrl"),
        ("group_ids", "groupIds"),
        ("is_admin", "isAdmin"),
        ("is_moderator", "isModerator"),
        ("opted_in_notifications", "optedInNotifications"),
        ("is_profile_activity_private", "isProfileActivityPrivate"),
    )

    def __init__(
        self,
        id=None,
        email=None,
        username=None,
        avatar=None,
        display_name=None,
        display_label=None,
        website_url=None,
        group_ids=None,
        is_admin=None,
        is_moderator=None,
        opted_in_notifications=None,
        is_profile_activity_private=None,
        **extra,
    ):
        self.id = None if id is None else str(id)
        self.email = email
        self.username = username
        self.avatar = avatar
        self.display_name = display_name
        self.display_label = display_label
        self.website_url = website_url
        self.group_ids = group_ids
        self.is_admin = is_admin
        self.is_moderator = is_moderator
        self.opted_in_notifications = opted_in_notifications
        self.is_profile_activity_private = is_profile_activity_private
        # Escape hatch for widget SSO fields not modeled above; assumed to be
        # already wire-ready (camelCase) keys. None values are dropped.
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

    def as_json_base64(self) -> str:
        return base64.b64encode(self.toJSON().encode("utf-8")).decode("utf-8")
