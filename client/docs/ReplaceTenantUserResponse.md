# ReplaceTenantUserResponse


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
from client.models.replace_tenant_user_response import ReplaceTenantUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReplaceTenantUserResponse from a JSON string
replace_tenant_user_response_instance = ReplaceTenantUserResponse.from_json(json)
# print the JSON string representation of the object
print(ReplaceTenantUserResponse.to_json())

# convert the object into a dict
replace_tenant_user_response_dict = replace_tenant_user_response_instance.to_dict()
# create an instance of ReplaceTenantUserResponse from a dict
replace_tenant_user_response_from_dict = ReplaceTenantUserResponse.from_dict(replace_tenant_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


