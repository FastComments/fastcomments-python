# GetTenantsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**tenants** | [**List[APITenant]**](APITenant.md) |  | 

## Example

```python
from client.models.get_tenants_response import GetTenantsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTenantsResponse from a JSON string
get_tenants_response_instance = GetTenantsResponse.from_json(json)
# print the JSON string representation of the object
print(GetTenantsResponse.to_json())

# convert the object into a dict
get_tenants_response_dict = get_tenants_response_instance.to_dict()
# create an instance of GetTenantsResponse from a dict
get_tenants_response_from_dict = GetTenantsResponse.from_dict(get_tenants_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


