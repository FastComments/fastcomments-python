# ReplaceTenantPackageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.replace_tenant_package_response import ReplaceTenantPackageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReplaceTenantPackageResponse from a JSON string
replace_tenant_package_response_instance = ReplaceTenantPackageResponse.from_json(json)
# print the JSON string representation of the object
print(ReplaceTenantPackageResponse.to_json())

# convert the object into a dict
replace_tenant_package_response_dict = replace_tenant_package_response_instance.to_dict()
# create an instance of ReplaceTenantPackageResponse from a dict
replace_tenant_package_response_from_dict = ReplaceTenantPackageResponse.from_dict(replace_tenant_package_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


