# GetTenantUserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**tenant_user** | [**User**](User.md) |  | 

## Example

```python
from client.models.get_tenant_user_response import GetTenantUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTenantUserResponse from a JSON string
get_tenant_user_response_instance = GetTenantUserResponse.from_json(json)
# print the JSON string representation of the object
print(GetTenantUserResponse.to_json())

# convert the object into a dict
get_tenant_user_response_dict = get_tenant_user_response_instance.to_dict()
# create an instance of GetTenantUserResponse from a dict
get_tenant_user_response_from_dict = GetTenantUserResponse.from_dict(get_tenant_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


