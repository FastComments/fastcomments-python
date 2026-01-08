# GetTenantResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**tenant** | [**APITenant**](APITenant.md) |  | 

## Example

```python
from client.models.get_tenant_response import GetTenantResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTenantResponse from a JSON string
get_tenant_response_instance = GetTenantResponse.from_json(json)
# print the JSON string representation of the object
print(GetTenantResponse.to_json())

# convert the object into a dict
get_tenant_response_dict = get_tenant_response_instance.to_dict()
# create an instance of GetTenantResponse from a dict
get_tenant_response_from_dict = GetTenantResponse.from_dict(get_tenant_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


