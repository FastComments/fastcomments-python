# UpdateUserBadgeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
from client.models.update_user_badge_response import UpdateUserBadgeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserBadgeResponse from a JSON string
update_user_badge_response_instance = UpdateUserBadgeResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateUserBadgeResponse.to_json())

# convert the object into a dict
update_user_badge_response_dict = update_user_badge_response_instance.to_dict()
# create an instance of UpdateUserBadgeResponse from a dict
update_user_badge_response_from_dict = UpdateUserBadgeResponse.from_dict(update_user_badge_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


