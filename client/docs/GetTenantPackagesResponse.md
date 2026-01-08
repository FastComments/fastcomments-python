# GetTenantPackagesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**tenant_packages** | [**List[TenantPackage]**](TenantPackage.md) |  | 

## Example

```python
from client.models.get_tenant_packages_response import GetTenantPackagesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTenantPackagesResponse from a JSON string
get_tenant_packages_response_instance = GetTenantPackagesResponse.from_json(json)
# print the JSON string representation of the object
print(GetTenantPackagesResponse.to_json())

# convert the object into a dict
get_tenant_packages_response_dict = get_tenant_packages_response_instance.to_dict()
# create an instance of GetTenantPackagesResponse from a dict
get_tenant_packages_response_from_dict = GetTenantPackagesResponse.from_dict(get_tenant_packages_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


