"""Type-safe environment variable access for tests."""

import os
from typing import Optional


def get_required_env_var(name: str) -> str:
    """Get a required environment variable or raise an error if not set."""
    value = os.getenv(name)
    if not value:
        raise ValueError(
            f"Required environment variable {name} is not set. "
            "Please check your test environment configuration."
        )
    return value


def get_optional_env_var(name: str, default_value: str) -> str:
    """Get an optional environment variable or return the default value."""
    return os.getenv(name, default_value)


# Test environment configuration.
# Unit tests (SSO signing) run fully offline, so credentials are optional here;
# integration tests skip themselves when real credentials are absent.
API_KEY = get_optional_env_var("FASTCOMMENTS_API_KEY", "test-api-secret")
TENANT_ID = get_optional_env_var("FASTCOMMENTS_TENANT_ID", "demo")
BASE_URL = get_optional_env_var("FASTCOMMENTS_BASE_URL", "https://fastcomments.com")

# True only when real credentials were supplied (used to gate integration tests).
HAS_CREDENTIALS = bool(os.getenv("FASTCOMMENTS_API_KEY") and os.getenv("FASTCOMMENTS_TENANT_ID"))
