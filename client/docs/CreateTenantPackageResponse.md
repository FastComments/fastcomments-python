# CreateTenantPackageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**tenant_package** | [**TenantPackage**](TenantPackage.md) |  | 

## Example

```python
from client.models.create_tenant_package_response import CreateTenantPackageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTenantPackageResponse from a JSON string
create_tenant_package_response_instance = CreateTenantPackageResponse.from_json(json)
# print the JSON string representation of the object
print(CreateTenantPackageResponse.to_json())

# convert the object into a dict
create_tenant_package_response_dict = create_tenant_package_response_instance.to_dict()
# create an instance of CreateTenantPackageResponse from a dict
create_tenant_package_response_from_dict = CreateTenantPackageResponse.from_dict(create_tenant_package_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


