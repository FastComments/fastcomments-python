# APITenantDailyUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**year_number** | **float** |  | 
**month_number** | **float** |  | 
**day_number** | **float** |  | 
**comment_fetch_count** | **float** |  | 
**comment_create_count** | **float** |  | 
**conversation_create_count** | **float** |  | 
**vote_count** | **float** |  | 
**account_created_count** | **float** |  | 
**user_mention_search** | **float** |  | 
**hash_tag_search** | **float** |  | 
**gif_search_trending** | **float** |  | 
**gif_search** | **float** |  | 
**api_credits_used** | **float** |  | 
**created_at** | **datetime** |  | 
**billed** | **bool** |  | 
**ignored** | **bool** |  | 
**api_error_count** | **float** |  | 

## Example

```python
from client.models.api_tenant_daily_usage import APITenantDailyUsage

# TODO update the JSON string below
json = "{}"
# create an instance of APITenantDailyUsage from a JSON string
api_tenant_daily_usage_instance = APITenantDailyUsage.from_json(json)
# print the JSON string representation of the object
print(APITenantDailyUsage.to_json())

# convert the object into a dict
api_tenant_daily_usage_dict = api_tenant_daily_usage_instance.to_dict()
# create an instance of APITenantDailyUsage from a dict
api_tenant_daily_usage_from_dict = APITenantDailyUsage.from_dict(api_tenant_daily_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


