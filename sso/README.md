# Core Library (`sso`)

Hand-written, pure-stdlib utilities for authenticating your users to FastComments.
Nothing here is generated, and nothing here talks to the network - these classes
only build the token you hand to the comment widget or pass as an API `sso`
parameter.

```python
from sso import (
    FastCommentsSSO,
    SecureSSOUserData,
    SimpleSSOUserData,
    SecureSSOPayload,
    create_verification_hash,
    CreateHashError,
)
```

## Secure SSO vs Simple SSO

**Secure SSO** signs the user's identity with your API secret, so the server can
trust it. Use it in production.

**Simple SSO** sends an unsigned username. Anyone who can read your page can
impersonate any user, so it is only appropriate for local testing and demos.

## Secure SSO

```python
from sso import FastCommentsSSO, SecureSSOUserData

user_data = SecureSSOUserData(
    id="user-1234",              # required, stringified for you
    email="jane@example.com",
    username="jane",
    avatar="https://example.com/jane.png",
    display_name="Jane Doe",
)

sso = FastCommentsSSO.new_secure("YOUR_API_SECRET", user_data)
sso_token = sso.create_token()
```

Pass `sso_token` to the widget as `config.sso`, or to any `ModerationApi` /
`PublicApi` method that accepts an `sso` argument.

`new_secure` stamps the payload with the current time in **epoch milliseconds**
and HMAC-SHA256s `f"{timestamp}{userDataJSONBase64}"` with your API secret. The
server rejects payloads more than two days old, and it hashes that exact string,
so a timestamp in seconds fails verification.

### `SecureSSOUserData`

`id` is the only required field, and it is always serialized as a string. Unset
optionals are omitted from the payload rather than sent as `null`.

| Constructor argument | Wire key |
|---|---|
| `id` | `id` |
| `email` | `email` |
| `username` | `username` |
| `avatar` | `avatar` |
| `display_name` | `displayName` |
| `display_label` | `displayLabel` |
| `website_url` | `websiteUrl` |
| `group_ids` | `groupIds` |
| `is_admin` | `isAdmin` |
| `is_moderator` | `isModerator` |
| `opted_in_notifications` | `optedInNotifications` |
| `is_profile_activity_private` | `isProfileActivityPrivate` |

Any extra keyword arguments pass straight through, so widget SSO fields not
modeled above can still be sent. They are assumed to already be wire-ready
(camelCase) keys, and `None` values are dropped.

Useful methods: `to_dict()`, `toJSON()` (compact JSON), and `as_json_base64()`.

### `SecureSSOPayload`

The signed object itself, in wire shape: `userDataJSONBase64`,
`verificationHash`, `timestamp`, plus `loginURL` / `logoutURL` when set. You get
one from `FastCommentsSSO.new_secure`; construct it directly only if you are
signing elsewhere.

```python
from sso import FastCommentsSSO, SecureSSOPayload

payload = SecureSSOPayload(user_data_b64, verification_hash, timestamp_ms)
sso = FastCommentsSSO.new_secure_with_urls(payload, login_url, logout_url)
```

`to_widget_dict()` returns the dict the widget expects at `config.sso`;
`toJSON()` returns the same thing serialized.

## Simple SSO

```python
from sso import FastCommentsSSO, SimpleSSOUserData

user_data = SimpleSSOUserData(username="jane", email="jane@example.com")
sso = FastCommentsSSO.new_simple(user_data)
sso_token = sso.create_token()
```

`SimpleSSOUserData` is keyed on `username` and supports `email`, `avatar`,
`website_url` (`websiteUrl`), and `display_name` (`displayName`), with the same
"omit unset, pass through extras" behavior as `SecureSSOUserData`.

## Login and logout URLs

Both constructors accept `login_url` and `logout_url`. When set, they are
included in the payload as `loginURL` / `logoutURL`. The widget redirects an
unauthenticated visitor to `loginURL` when they try to comment; with no
`loginURL` it shows its own "log in" text instead.

```python
sso = FastCommentsSSO.new_secure(
    "YOUR_API_SECRET",
    user_data,
    login_url="https://example.com/login",
    logout_url="https://example.com/logout",
)
```

## Token caching and swapping users

`create_token()` serializes on every call. `prepare_to_send()` serializes once
and caches the result, which is what you want when rendering the same user
repeatedly.

When the logged-in user changes, replace the data rather than reusing the
instance's cached token - both setters reset the cache for you:

```python
sso.set_secure_sso_payload(new_payload)   # switches to Secure SSO
sso.set_simple_sso_user_data(new_data)    # switches to Simple SSO
sso.reset_token()                         # or clear the cache by hand
```

`create_token()` raises `ValueError` if neither a secure payload nor simple user
data is set.

## Signing by hand

`create_verification_hash(api_key, timestamp, user_data_json_base64)` is the
HMAC-SHA256 helper `new_secure` uses, returned as a lowercase hex string. It
raises `CreateHashError` on failure.

```python
from sso import create_verification_hash, CreateHashError

try:
    hash = create_verification_hash(api_secret, timestamp_ms, user_data_b64)
except CreateHashError as e:
    ...
```

## Keeping the secret on the server

Your API secret must never reach the browser. Build the token in your backend
and send only the finished token to the page. Anyone holding the secret can
sign a payload for any user, including admins and moderators.

## See also

- [API Client Library Docs](../client/README.md)
- [Project README](../README.md)
