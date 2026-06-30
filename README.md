# fastcomments
The FastComments Python SDK. You can use this to build secure and scalable backend applications that interact with FastComments, or build reactive client applications.

## Installation

### PyPI

```bash
pip install fastcomments
```

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
config.host = "https://fastcomments.com/api"

# REQUIRED: Set your API key (get this from your FastComments dashboard)
config.api_key = {"ApiKeyAuth": "YOUR_API_KEY_HERE"}

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
config.host = "https://fastcomments.com/api"

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
config.host = "https://fastcomments.com/api"

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

# Create user data
user_data = SecureSSOUserData(
    user_id="user-123",
    email="user@example.com",
    username="johndoe",
    avatar="https://example.com/avatar.jpg"
)

# Create SSO instance with your API secret
sso = FastCommentsSSO.new_secure(
    api_secret="YOUR_API_SECRET",
    user_data=user_data
)

# Generate the SSO token
sso_token = sso.create_token()

# Use this token in your frontend or pass to API calls
print(f"SSO Token: {sso_token}")
```

For simple SSO (less secure, for testing):

```python
from sso import FastCommentsSSO, SimpleSSOUserData

user_data = SimpleSSOUserData(
    user_id="user-123",
    email="user@example.com"
)

sso = FastCommentsSSO.new_simple(user_data)
sso_token = sso.create_token()
```

### Common Issues

1. **401 "missing-api-key" error**: Make sure you set `config.api_key = {"ApiKeyAuth": "YOUR_KEY"}` before creating the DefaultApi instance.
2. **Wrong API class**: Use `DefaultApi` for server-side authenticated requests, `PublicApi` for client-side/public requests, and `ModerationApi` for moderator dashboard requests.
3. **Import errors**: Make sure you're importing from the correct module:
   - API client: `from client import ...`
   - SSO utilities: `from sso import ...`

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
- urllib3 >= 1.25.3
- python-dateutil >= 2.8.2
- pydantic >= 2.0.0
- typing-extensions >= 4.0.0

## License

MIT

## Support

- [Documentation](https://docs.fastcomments.com)
- [GitHub Issues](https://github.com/fastcomments/fastcomments-python/issues)
- [FastComments Support](https://fastcomments.com/auth/my-account/help)
