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


# Test environment configuration
API_KEY = get_required_env_var("FASTCOMMENTS_API_KEY")
TENANT_ID = get_required_env_var("FASTCOMMENTS_TENANT_ID")
BASE_URL = get_optional_env_var("FASTCOMMENTS_BASE_URL", "https://fastcomments.com")
