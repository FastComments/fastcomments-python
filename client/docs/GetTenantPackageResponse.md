# GetTenantPackageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**tenant_package** | [**TenantPackage**](TenantPackage.md) |  | 

## Example

```python
from client.models.get_tenant_package_response import GetTenantPackageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTenantPackageResponse from a JSON string
get_tenant_package_response_instance = GetTenantPackageResponse.from_json(json)
# print the JSON string representation of the object
print(GetTenantPackageResponse.to_json())

# convert the object into a dict
get_tenant_package_response_dict = get_tenant_package_response_instance.to_dict()
# create an instance of GetTenantPackageResponse from a dict
get_tenant_package_response_from_dict = GetTenantPackageResponse.from_dict(get_tenant_package_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


