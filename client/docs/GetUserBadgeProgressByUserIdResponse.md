# GetUserBadgeProgressByUserIdResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**user_badge_progress** | [**UserBadgeProgress**](UserBadgeProgress.md) |  | 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.get_user_badge_progress_by_user_id_response import GetUserBadgeProgressByUserIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserBadgeProgressByUserIdResponse from a JSON string
get_user_badge_progress_by_user_id_response_instance = GetUserBadgeProgressByUserIdResponse.from_json(json)
# print the JSON string representation of the object
print(GetUserBadgeProgressByUserIdResponse.to_json())

# convert the object into a dict
get_user_badge_progress_by_user_id_response_dict = get_user_badge_progress_by_user_id_response_instance.to_dict()
# create an instance of GetUserBadgeProgressByUserIdResponse from a dict
get_user_badge_progress_by_user_id_response_from_dict = GetUserBadgeProgressByUserIdResponse.from_dict(get_user_badge_progress_by_user_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


