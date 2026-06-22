# GetTenantDailyUsagesResponse1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**tenant_daily_usages** | [**List[APITenantDailyUsage]**](APITenantDailyUsage.md) |  | 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.get_tenant_daily_usages_response1 import GetTenantDailyUsagesResponse1

# TODO update the JSON string below
json = "{}"
# create an instance of GetTenantDailyUsagesResponse1 from a JSON string
get_tenant_daily_usages_response1_instance = GetTenantDailyUsagesResponse1.from_json(json)
# print the JSON string representation of the object
print(GetTenantDailyUsagesResponse1.to_json())

# convert the object into a dict
get_tenant_daily_usages_response1_dict = get_tenant_daily_usages_response1_instance.to_dict()
# create an instance of GetTenantDailyUsagesResponse1 from a dict
get_tenant_daily_usages_response1_from_dict = GetTenantDailyUsagesResponse1.from_dict(get_tenant_daily_usages_response1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


