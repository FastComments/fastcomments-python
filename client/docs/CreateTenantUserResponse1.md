# CreateTenantUserResponse1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**tenant_user** | [**User**](User.md) |  | 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.create_tenant_user_response1 import CreateTenantUserResponse1

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTenantUserResponse1 from a JSON string
create_tenant_user_response1_instance = CreateTenantUserResponse1.from_json(json)
# print the JSON string representation of the object
print(CreateTenantUserResponse1.to_json())

# convert the object into a dict
create_tenant_user_response1_dict = create_tenant_user_response1_instance.to_dict()
# create an instance of CreateTenantUserResponse1 from a dict
create_tenant_user_response1_from_dict = CreateTenantUserResponse1.from_dict(create_tenant_user_response1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


