"""Unit tests for FastComments SSO functionality.

These assert the on-the-wire format the FastComments server actually verifies
(see server util/sso-utils.ts decryptSSOPayload): the signed message is
`str(timestamp_ms) + userDataJSONBase64`, the payload keys are camelCase
(userDataJSONBase64/verificationHash/timestamp), the user object is keyed on
`id`, and the timestamp is epoch milliseconds. The pinned parity vector below
must stay byte-identical across the JS/PHP/Java SDKs.
"""

import json
import base64
import hmac
import hashlib
import time
import pytest

from sso import (
    FastCommentsSSO,
    SecureSSOPayload,
    SecureSSOUserData,
    SimpleSSOUserData,
    create_verification_hash,
    CreateHashError,
)


# Pinned known-answer vector. Regenerate with the same algorithm in any SDK:
#   msg = str(TS) + base64(compact_json(USER)); HMAC-SHA256(SECRET, msg).hexdigest()
PARITY_SECRET = "test-api-secret"
PARITY_TS = 1700000000000  # epoch MILLISECONDS
PARITY_USER_JSON = '{"id":"123","email":"test@example.com","username":"tester"}'
PARITY_USER_B64 = base64.b64encode(PARITY_USER_JSON.encode("utf-8")).decode("utf-8")
PARITY_HASH = "f7e13d510e7f0cb11f027ce8161b8dc0f380df4aa85213ed15a973e34cb9dc2f"


class TestHelpers:
    """Test helper functions."""

    def test_create_verification_hash(self):
        """create_verification_hash produces lowercase-hex HMAC-SHA256."""
        timestamp = 1700000000000
        user_data = "test_data_base64"

        result = create_verification_hash(PARITY_SECRET, timestamp, user_data)

        assert isinstance(result, str)
        assert len(result) == 64
        assert result == result.lower()

        message_str = f"{timestamp}{user_data}"
        expected = hmac.new(
            PARITY_SECRET.encode("utf-8"),
            message_str.encode("utf-8"),
            hashlib.sha256,
        ).hexdigest()
        assert result == expected

    def test_parity_vector(self):
        """The signer must match the pinned cross-SDK vector byte-for-byte."""
        assert create_verification_hash(PARITY_SECRET, PARITY_TS, PARITY_USER_B64) == PARITY_HASH

    def test_create_verification_hash_with_empty_api_key(self):
        result = create_verification_hash("", 1700000000000, "test_data")
        assert isinstance(result, str)
        assert len(result) == 64


class TestSecureSSOUserData:
    """Test SecureSSOUserData class."""

    def test_serializes_id_key_not_user_id(self):
        """The server requires `id`; `user_id` must never appear on the wire."""
        user = SecureSSOUserData(id="123", email="test@example.com", username="tester")
        parsed = json.loads(user.toJSON())

        assert parsed["id"] == "123"
        assert "user_id" not in parsed
        assert parsed["email"] == "test@example.com"
        assert parsed["username"] == "tester"

    def test_matches_parity_json(self):
        """Compact serialization must equal the pinned vector's base64."""
        user = SecureSSOUserData(id="123", email="test@example.com", username="tester")
        assert user.as_json_base64() == PARITY_USER_B64

    def test_id_is_stringified(self):
        user = SecureSSOUserData(id=123, email="a@b.com", username="u")
        parsed = json.loads(user.toJSON())
        assert parsed["id"] == "123"
        assert isinstance(parsed["id"], str)

    def test_optional_fields_use_camelcase_and_drop_none(self):
        user = SecureSSOUserData(
            id="1",
            email="a@b.com",
            username="u",
            avatar="https://x/y.png",
            display_name="Display Name",
            website_url="https://site",
            group_ids=["g1", "g2"],
            is_admin=True,
            is_moderator=False,
            opted_in_notifications=True,
        )
        parsed = json.loads(user.toJSON())

        assert parsed["displayName"] == "Display Name"
        assert parsed["websiteUrl"] == "https://site"
        assert parsed["groupIds"] == ["g1", "g2"]
        assert parsed["isAdmin"] is True
        assert parsed["isModerator"] is False  # False is kept, only None is dropped
        assert parsed["optedInNotifications"] is True
        # snake_case keys must never leak onto the wire
        assert "display_name" not in parsed
        assert "website_url" not in parsed
        assert "group_ids" not in parsed

    def test_none_optionals_are_omitted(self):
        user = SecureSSOUserData(id="1", email="a@b.com", username="u")
        parsed = json.loads(user.toJSON())
        assert set(parsed.keys()) == {"id", "email", "username"}


class TestSimpleSSOUserData:
    """Test SimpleSSOUserData class."""

    def test_includes_username(self):
        """Simple SSO's simpleSSO object is keyed on username."""
        user = SimpleSSOUserData(username="tester", email="test@example.com")
        parsed = json.loads(user.toJSON())

        assert parsed["username"] == "tester"
        assert parsed["email"] == "test@example.com"
        assert "user_id" not in parsed

    def test_optional_fields(self):
        user = SimpleSSOUserData(
            username="u",
            email="a@b.com",
            avatar="https://x/y.png",
            website_url="https://site",
        )
        parsed = json.loads(user.toJSON())
        assert parsed["avatar"] == "https://x/y.png"
        assert parsed["websiteUrl"] == "https://site"


class TestSecureSSOPayload:
    """Test SecureSSOPayload class (camelCase wire format)."""

    def test_to_widget_dict_is_camelcase(self):
        payload = SecureSSOPayload("theb64", "thehash", 1700000000000)
        d = payload.to_widget_dict()

        assert d["userDataJSONBase64"] == "theb64"
        assert d["verificationHash"] == "thehash"
        assert d["timestamp"] == 1700000000000
        assert "user_data_json_base64" not in d
        assert "verification_hash" not in d

    def test_to_json_is_camelcase(self):
        payload = SecureSSOPayload("theb64", "thehash", 1700000000000)
        parsed = json.loads(payload.toJSON())
        assert parsed["userDataJSONBase64"] == "theb64"
        assert parsed["verificationHash"] == "thehash"
        assert parsed["timestamp"] == 1700000000000

    def test_login_logout_urls_included_when_set(self):
        payload = SecureSSOPayload(
            "theb64", "thehash", 1700000000000, login_url="/login", logout_url="/logout"
        )
        d = payload.to_widget_dict()
        assert d["loginURL"] == "/login"
        assert d["logoutURL"] == "/logout"


class TestFastCommentsSSO:
    """Test FastCommentsSSO class."""

    def test_new_secure_uses_millisecond_timestamp(self):
        """Timestamp must be epoch ms (~1.7e12), not seconds (~1.7e9)."""
        user = SecureSSOUserData(id="1", email="a@b.com", username="u")
        before = int(time.time() * 1000)
        sso = FastCommentsSSO.new_secure(PARITY_SECRET, user)
        after = int(time.time() * 1000)

        ts = sso.secure_sso_payload.timestamp
        assert ts >= 10 ** 12  # milliseconds, not seconds
        assert before <= ts <= after

    def test_secure_token_is_camelcase_and_verifies(self):
        user = SecureSSOUserData(id="user-123", email="a@b.com", username="u")
        sso = FastCommentsSSO.new_secure(PARITY_SECRET, user)
        parsed = json.loads(sso.create_token())

        assert "userDataJSONBase64" in parsed
        assert "verificationHash" in parsed
        assert "timestamp" in parsed

        # The hash must verify against the exact base64 that is sent.
        expected = create_verification_hash(
            PARITY_SECRET, parsed["timestamp"], parsed["userDataJSONBase64"]
        )
        assert parsed["verificationHash"] == expected

        decoded = json.loads(base64.b64decode(parsed["userDataJSONBase64"]))
        assert decoded["id"] == "user-123"

    def test_new_simple_token_includes_username(self):
        user = SimpleSSOUserData(username="tester", email="a@b.com")
        sso = FastCommentsSSO.new_simple(user)
        parsed = json.loads(sso.create_token())
        assert parsed["username"] == "tester"
        assert parsed["email"] == "a@b.com"

    def test_secure_sso_with_urls(self):
        user = SecureSSOUserData(id="1", email="a@b.com", username="u")
        sso = FastCommentsSSO.new_secure(PARITY_SECRET, user, login_url="/login", logout_url="/logout")
        assert sso.login_url == "/login"
        assert sso.logout_url == "/logout"
        assert sso.secure_sso_payload.to_widget_dict()["loginURL"] == "/login"

    def test_no_data_raises_error(self):
        sso = FastCommentsSSO(None, None)
        with pytest.raises(ValueError, match="No user data provided"):
            sso.create_token()

    def test_token_caching(self):
        user = SimpleSSOUserData(username="u", email="a@b.com")
        sso = FastCommentsSSO.new_simple(user)
        assert sso.prepare_to_send() == sso.prepare_to_send()

    def test_reset_token(self):
        user = SimpleSSOUserData(username="u", email="a@b.com")
        sso = FastCommentsSSO.new_simple(user)
        sso.prepare_to_send()
        sso.reset_token()
        assert sso.cached_token is None

    def test_set_secure_sso_payload(self):
        sso = FastCommentsSSO.new_simple(SimpleSSOUserData(username="u", email="a@b.com"))
        secure_user = SecureSSOUserData(id="1", email="a@b.com", username="u")
        payload = FastCommentsSSO.new_secure(PARITY_SECRET, secure_user).secure_sso_payload
        sso.set_secure_sso_payload(payload)
        assert sso.secure_sso_payload is not None
        assert sso.simple_sso_user_data is None

    def test_set_simple_sso_user_data(self):
        secure_user = SecureSSOUserData(id="1", email="a@b.com", username="u")
        sso = FastCommentsSSO.new_secure(PARITY_SECRET, secure_user)
        sso.set_simple_sso_user_data(SimpleSSOUserData(username="u", email="a@b.com"))
        assert sso.simple_sso_user_data is not None
        assert sso.secure_sso_payload is None
