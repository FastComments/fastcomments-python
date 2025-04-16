from sso.fastcomments_sso import FastCommentsSSO
from sso.simple_sso_user_data import SimpleSSOUserData


def main():
    api_key = "your_api_key_here"
    # This should be done server side for security
    user_data = SimpleSSOUserData(
        "user-123",
        "email@example.com",
        "Avatar"
    )
    
    # Create SSO config with payload
    sso = FastCommentsSSO.new_simple(user_data)
    
    tenant_id = "tenant-123"
    url_id = "123"
    token = sso.create_token()
    
    # Create configuration
    
    # Interact with client