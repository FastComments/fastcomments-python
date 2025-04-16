from sso.fastcomments_sso import FastCommentsSSO
from sso.secure_sso_user_data import SecureSSOUserData


def main():
    api_key = "your_api_key_here"
    # This should be done server side for security
    user_data = SecureSSOUserData(
        "user-123",
        "email@example.com",
        "John Doe",
        "Avatar"
    )
    
    # Create SSO config with payload
    sso = FastCommentsSSO.new_secure(api_key, user_data)
    
    tenant_id = "tenant-123"
    url_id = "123"
    token = sso.create_token()
    
    # Create configuration
    
    # Interact with client