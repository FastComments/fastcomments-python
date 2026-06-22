# GetTenantPackagesResponse1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**tenant_packages** | [**List[TenantPackage]**](TenantPackage.md) |  | 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.get_tenant_packages_response1 import GetTenantPackagesResponse1

# TODO update the JSON string below
json = "{}"
# create an instance of GetTenantPackagesResponse1 from a JSON string
get_tenant_packages_response1_instance = GetTenantPackagesResponse1.from_json(json)
# print the JSON string representation of the object
print(GetTenantPackagesResponse1.to_json())

# convert the object into a dict
get_tenant_packages_response1_dict = get_tenant_packages_response1_instance.to_dict()
# create an instance of GetTenantPackagesResponse1 from a dict
get_tenant_packages_response1_from_dict = GetTenantPackagesResponse1.from_dict(get_tenant_packages_response1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


