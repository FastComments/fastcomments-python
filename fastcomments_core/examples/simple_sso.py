from fastcomments_client.api import public_api
from fastcomments_core.sso.fastcomments_sso import FastCommentsSSO
from fastcomments_core.sso.simple_sso_user_data import SimpleSSOUserData


def main():
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
    
    # Interact with client
    pub = public_api.PublicApi()
    res = pub.get_comments_public(tenant_id=tenant_id, url_id=url_id, sso=token)
    print(res)
    
main()