# GetUserBanPreferenceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preferences** | [**APIModerateUserBanPreferences**](APIModerateUserBanPreferences.md) |  | 
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
from client.models.get_user_ban_preference_response import GetUserBanPreferenceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserBanPreferenceResponse from a JSON string
get_user_ban_preference_response_instance = GetUserBanPreferenceResponse.from_json(json)
# print the JSON string representation of the object
print(GetUserBanPreferenceResponse.to_json())

# convert the object into a dict
get_user_ban_preference_response_dict = get_user_ban_preference_response_instance.to_dict()
# create an instance of GetUserBanPreferenceResponse from a dict
get_user_ban_preference_response_from_dict = GetUserBanPreferenceResponse.from_dict(get_user_ban_preference_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


