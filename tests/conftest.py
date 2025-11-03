"""Pytest configuration and fixtures for FastComments tests."""

import pytest
import sys
from pathlib import Path

# Add the parent directory to the path so we can import sso and client modules
sys.path.insert(0, str(Path(__file__).parent.parent))

from tests.env import API_KEY, TENANT_ID, BASE_URL


@pytest.fixture
def api_key():
    """Provide the API key for tests."""
    return API_KEY


@pytest.fixture
def tenant_id():
    """Provide the tenant ID for tests."""
    return TENANT_ID


@pytest.fixture
def base_url():
    """Provide the base URL for tests."""
    return BASE_URL


@pytest.fixture
def test_user_data():
    """Provide sample user data for SSO tests."""
    return {
        "user_id": "test-user-123",
        "email": "test@example.com",
        "username": "testuser",
        "avatar": "https://example.com/avatar.jpg"
    }
