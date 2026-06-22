# GetUserBadgeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**user_badge** | [**UserBadge**](UserBadge.md) |  | 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.get_user_badge_response import GetUserBadgeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserBadgeResponse from a JSON string
get_user_badge_response_instance = GetUserBadgeResponse.from_json(json)
# print the JSON string representation of the object
print(GetUserBadgeResponse.to_json())

# convert the object into a dict
get_user_badge_response_dict = get_user_badge_response_instance.to_dict()
# create an instance of GetUserBadgeResponse from a dict
get_user_badge_response_from_dict = GetUserBadgeResponse.from_dict(get_user_badge_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


