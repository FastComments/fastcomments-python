# APIModerateGetUserBanPreferencesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preferences** | [**APIModerateUserBanPreferences**](APIModerateUserBanPreferences.md) |  | 
**status** | [**APIStatus**](APIStatus.md) |  | 

## Example

```python
from client.models.api_moderate_get_user_ban_preferences_response import APIModerateGetUserBanPreferencesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of APIModerateGetUserBanPreferencesResponse from a JSON string
api_moderate_get_user_ban_preferences_response_instance = APIModerateGetUserBanPreferencesResponse.from_json(json)
# print the JSON string representation of the object
print(APIModerateGetUserBanPreferencesResponse.to_json())

# convert the object into a dict
api_moderate_get_user_ban_preferences_response_dict = api_moderate_get_user_ban_preferences_response_instance.to_dict()
# create an instance of APIModerateGetUserBanPreferencesResponse from a dict
api_moderate_get_user_ban_preferences_response_from_dict = APIModerateGetUserBanPreferencesResponse.from_dict(api_moderate_get_user_ban_preferences_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


