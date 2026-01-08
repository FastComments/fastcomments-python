# GetTenantDailyUsagesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**tenant_daily_usages** | [**List[APITenantDailyUsage]**](APITenantDailyUsage.md) |  | 

## Example

```python
from client.models.get_tenant_daily_usages_response import GetTenantDailyUsagesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTenantDailyUsagesResponse from a JSON string
get_tenant_daily_usages_response_instance = GetTenantDailyUsagesResponse.from_json(json)
# print the JSON string representation of the object
print(GetTenantDailyUsagesResponse.to_json())

# convert the object into a dict
get_tenant_daily_usages_response_dict = get_tenant_daily_usages_response_instance.to_dict()
# create an instance of GetTenantDailyUsagesResponse from a dict
get_tenant_daily_usages_response_from_dict = GetTenantDailyUsagesResponse.from_dict(get_tenant_daily_usages_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


