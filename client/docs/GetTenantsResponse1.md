# GetTenantsResponse1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**tenants** | [**List[APITenant]**](APITenant.md) |  | 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.get_tenants_response1 import GetTenantsResponse1

# TODO update the JSON string below
json = "{}"
# create an instance of GetTenantsResponse1 from a JSON string
get_tenants_response1_instance = GetTenantsResponse1.from_json(json)
# print the JSON string representation of the object
print(GetTenantsResponse1.to_json())

# convert the object into a dict
get_tenants_response1_dict = get_tenants_response1_instance.to_dict()
# create an instance of GetTenantsResponse1 from a dict
get_tenants_response1_from_dict = GetTenantsResponse1.from_dict(get_tenants_response1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


