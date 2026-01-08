# GetTenantUsersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**tenant_users** | [**List[User]**](User.md) |  | 

## Example

```python
from client.models.get_tenant_users_response import GetTenantUsersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTenantUsersResponse from a JSON string
get_tenant_users_response_instance = GetTenantUsersResponse.from_json(json)
# print the JSON string representation of the object
print(GetTenantUsersResponse.to_json())

# convert the object into a dict
get_tenant_users_response_dict = get_tenant_users_response_instance.to_dict()
# create an instance of GetTenantUsersResponse from a dict
get_tenant_users_response_from_dict = GetTenantUsersResponse.from_dict(get_tenant_users_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


