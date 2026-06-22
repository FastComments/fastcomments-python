# GetManualBadgesForUserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**badges** | [**List[UserBadge]**](UserBadge.md) |  | 
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
from client.models.get_manual_badges_for_user_response import GetManualBadgesForUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetManualBadgesForUserResponse from a JSON string
get_manual_badges_for_user_response_instance = GetManualBadgesForUserResponse.from_json(json)
# print the JSON string representation of the object
print(GetManualBadgesForUserResponse.to_json())

# convert the object into a dict
get_manual_badges_for_user_response_dict = get_manual_badges_for_user_response_instance.to_dict()
# create an instance of GetManualBadgesForUserResponse from a dict
get_manual_badges_for_user_response_from_dict = GetManualBadgesForUserResponse.from_dict(get_manual_badges_for_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


