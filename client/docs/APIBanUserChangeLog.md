# APIBanUserChangeLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_banned_user_id** | **str** |  | [optional] 
**updated_banned_user_id** | **str** |  | [optional] 
**deleted_banned_users** | [**List[APIBannedUser]**](APIBannedUser.md) |  | [optional] 
**changed_values_before** | [**APIBanUserChangedValues**](APIBanUserChangedValues.md) |  | [optional] 

## Example

```python
from client.models.api_ban_user_change_log import APIBanUserChangeLog

# TODO update the JSON string below
json = "{}"
# create an instance of APIBanUserChangeLog from a JSON string
api_ban_user_change_log_instance = APIBanUserChangeLog.from_json(json)
# print the JSON string representation of the object
print(APIBanUserChangeLog.to_json())

# convert the object into a dict
api_ban_user_change_log_dict = api_ban_user_change_log_instance.to_dict()
# create an instance of APIBanUserChangeLog from a dict
api_ban_user_change_log_from_dict = APIBanUserChangeLog.from_dict(api_ban_user_change_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


