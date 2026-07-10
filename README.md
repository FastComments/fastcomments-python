# fastcomments
The FastComments Python SDK. You can use this to build secure and scalable backend applications that interact with FastComments, or build reactive client applications.

## Installation

### Install from GitHub

Install directly from a release tag (recommended, fully reproducible):

```bash
pip install git+https://github.com/fastcomments/fastcomments-python.git@v3.0.0
```

Pin the tag rather than a branch so builds are deterministic. The same form works in `requirements.txt`:

```
fastcomments @ git+https://github.com/fastcomments/fastcomments-python.git@v3.0.0
```

Each tagged [GitHub Release](https://github.com/fastcomments/fastcomments-python/releases) also has a built wheel attached if you prefer to install a binary artifact directly.

### Library Contents

This library contains two modules: the generated API client and the core Python library which contains hand-written utilities to make working with the API easier, including SSO support.

- [API Client Library Docs](./client/README.md)
- [Core Library Docs, Including SSO Examples](./sso/README.md)

### Public vs Secured APIs

For the API client, there are three classes, `DefaultApi`, `PublicApi`, and `ModerationApi`. The `DefaultApi` contains methods that require your API key, and `PublicApi` contains methods that can be made directly from a browser/mobile device/etc without authentication. The `ModerationApi` provides an extensive suite of live and fast moderation APIs. Every `ModerationApi` method accepts an `sso` parameter and can authenticate via SSO or a FastComments.com session cookie.

## Quick Start

### Using Authenticated APIs (DefaultApi)

**Important:** You must set your API key on the Configuration before making authenticated requests. If you don't, requests will fail with a 401 error.

```python
from client import ApiClient, Configuration, DefaultApi
from client.models import CreateAPISSOUserData

# Create and configure the API client
config = Configuration()
config.host = "https://fastcomments.com"

# REQUIRED: Set your API key (get this from your FastComments dashboard)
config.api_key = {"api_key": "YOUR_API_KEY_HERE"}

# Create the API instance with the configured client
api_client = ApiClient(configuration=config)
api = DefaultApi(api_client)

# Now you can make authenticated API calls
try:
    # Example: Add an SSO user
    user_data = CreateAPISSOUserData(
        id="user-123",
        email="user@example.com",
        display_name="John Doe"
    )

    response = api.add_sso_user("YOUR_TENANT_ID", user_data)
    print(f"User created: {response}")

except Exception as e:
    print(f"Error: {e}")
    # Common errors:
    # - 401: API key is missing or invalid
    # - 400: Request validation failed
```

### Using Public APIs (PublicApi)

Public endpoints don't require authentication:

```python
from client import ApiClient, Configuration, PublicApi

config = Configuration()
config.host = "https://fastcomments.com"

api_client = ApiClient(configuration=config)
public_api = PublicApi(api_client)

try:
    response = public_api.get_comments_public("YOUR_TENANT_ID", "page-url-id")
    print(response)
except Exception as e:
    print(f"Error: {e}")
```

### Using the Moderation Dashboard (ModerationApi)

The `ModerationApi` powers the moderator dashboard. Methods are called on behalf of a moderator by passing an `sso` token:

```python
from client import ApiClient, Configuration, ModerationApi
from client.api.moderation_api import GetCountOptions

config = Configuration()
config.host = "https://fastcomments.com"

api_client = ApiClient(configuration=config)
moderation_api = ModerationApi(api_client)

try:
    # Count the comments awaiting moderation
    response = moderation_api.get_count(GetCountOptions(sso="SSO_TOKEN"))
    print(response)
except Exception as e:
    print(f"Error: {e}")
```

### Using SSO (Single Sign-On)

The SDK includes utilities for generating secure SSO tokens:

```python
from sso import FastCommentsSSO, SecureSSOUserData

# Create user data (id, email, and username are required)
user_data = SecureSSOUserData(
    id="user-123",
    email="user@example.com",
    username="johndoe",
    avatar="https://example.com/avatar.jpg"
)

# Sign it with your API secret (HMAC-SHA256)
sso = FastCommentsSSO.new_secure("YOUR_API_SECRET", user_data)

# Generate the SSO token to pass to the widget or an API call
sso_token = sso.create_token()

# Use this token in your frontend or pass to API calls
print(f"SSO Token: {sso_token}")
```

For simple SSO (less secure, for testing):

```python
from sso import FastCommentsSSO, SimpleSSOUserData

user_data = SimpleSSOUserData(
    username="johndoe",
    email="user@example.com"
)

sso = FastCommentsSSO.new_simple(user_data)
sso_token = sso.create_token()
```

### Live Subscriptions (PubSub)

The `pubsub` module lets you subscribe to real-time comment events (new comments, votes, edits, notifications, etc.) over a WebSocket, mirroring the FastComments Java SDK's `LiveEventSubscriber`. It requires the `pubsub` extra, which adds a WebSocket client on top of the generated API client:

```bash
pip install "fastcomments[pubsub] @ git+https://github.com/fastcomments/fastcomments-python.git@v3.0.0"
```

```python
from pubsub import LiveEventSubscriber

subscriber = LiveEventSubscriber()

def handle_live_event(event):
    print(f"Live event: {event.type}")
    if event.comment:
        print(f"  comment: {event.comment.comment}")

result = subscriber.subscribe_to_changes(
    tenant_id_ws="YOUR_TENANT_ID",
    url_id="page-url-id",
    url_id_ws="page-url-id",
    user_id_ws="a-unique-presence-id",  # e.g. a UUID for this session
    handle_live_event=handle_live_event,
    on_connection_status_change=lambda connected, last_event_time: print(
        f"connected={connected}"
    ),
    region=None,  # set to "eu" for the EU region
)

# ...later, when you no longer want updates:
result.close()
```

The subscriber runs the connection on a background daemon thread, transparently reconnects with jitter, and fetches any events missed while disconnected from the event-log endpoint on reconnect. Pass an optional `can_see_comments` callback (`List[str] -> Dict[str, str]`, returning the ids the user may NOT see) to filter out events for comments the user is not allowed to view. Set `disable_live_commenting=True` to make `subscribe_to_changes` a no-op that returns `None`.

### Common Issues

1. **401 "missing-api-key" error**: Make sure you set `config.api_key = {"api_key": "YOUR_KEY"}` before creating the DefaultApi instance.
2. **Wrong API class**: Use `DefaultApi` for server-side authenticated requests, `PublicApi` for client-side/public requests, and `ModerationApi` for moderator dashboard requests.
3. **Import errors**: Make sure you're importing from the correct module:
   - API client: `from client import ...`
   - SSO utilities: `from sso import ...`
   - Live subscriptions: `from pubsub import ...` (needs the `pubsub` extra)

## Development

### Running Tests

```bash
# Set up environment variables
export FASTCOMMENTS_API_KEY="your-api-key"
export FASTCOMMENTS_TENANT_ID="your-tenant-id"

# Run tests
pytest tests/
```

### Regenerating the Client

To regenerate the API client from the latest OpenAPI specification:

```bash
./update.sh
```

This will:
1. Download the latest OpenAPI spec from a running FastComments server (or use local openapi.yaml)
2. Generate the Python client code
3. Flatten the directory structure
4. Clean up redundant configuration files

## Notes

### Broadcast IDs

You'll see you're supposed to pass a `broadcast_id` in some API calls. When you receive events, you'll get this ID back, so you know to ignore the event if you plan to optimistically apply changes on the client (which you'll probably want to do since it offers the best experience). Pass a UUID here. The ID should be unique enough to not occur twice in a browser session.

## Requirements

- Python >= 3.8

The base install is pure-stdlib and provides the SSO utilities. The generated
API client (`DefaultApi`/`PublicApi`/`ModerationApi`) needs the `client` extra,
which pulls in `urllib3 >= 1.25.3`, `python-dateutil >= 2.8.2`,
`pydantic >= 2.0.0`, and `typing-extensions >= 4.0.0`:

```bash
pip install "fastcomments[client] @ git+https://github.com/fastcomments/fastcomments-python.git@v3.0.0"
```

## License

MIT

## Support

- [Documentation](https://docs.fastcomments.com)
- [GitHub Issues](https://github.com/fastcomments/fastcomments-python/issues)
- [FastComments Support](https://fastcomments.com/auth/my-account/help)
