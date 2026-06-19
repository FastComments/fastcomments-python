# APIModerateUserBanPreferences


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**should_ban_email** | **bool** |  | 
**should_ban_by_ip** | **bool** |  | 
**last_ban_type** | **str** |  | 
**last_ban_duration** | **str** |  | 

## Example

```python
from client.models.api_moderate_user_ban_preferences import APIModerateUserBanPreferences

# TODO update the JSON string below
json = "{}"
# create an instance of APIModerateUserBanPreferences from a JSON string
api_moderate_user_ban_preferences_instance = APIModerateUserBanPreferences.from_json(json)
# print the JSON string representation of the object
print(APIModerateUserBanPreferences.to_json())

# convert the object into a dict
api_moderate_user_ban_preferences_dict = api_moderate_user_ban_preferences_instance.to_dict()
# create an instance of APIModerateUserBanPreferences from a dict
api_moderate_user_ban_preferences_from_dict = APIModerateUserBanPreferences.from_dict(api_moderate_user_ban_preferences_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


