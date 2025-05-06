# from core.fastcomments_client.openapi_client.api import public_api
# from client.openapi_client.configuration import Configuration

# from client.build.lib.openapi_client.api import public_api
# from client.build.lib.openapi_client.configuration import Configuration
from fastcomments_client.api import public_api
from fastcomments_core.sso.fastcomments_sso import FastCommentsSSO
from fastcomments_core.sso.secure_sso_user_data import SecureSSOUserData


def main():
    api_key = "your-api-key"
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

    # Interact with client

    pub = public_api.PublicApi()
    res = pub.get_comments_public(tenant_id=tenant_id, url_id=url_id, sso=token)
    print(res)

main()