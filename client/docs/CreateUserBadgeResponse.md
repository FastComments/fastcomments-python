# CreateUserBadgeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**user_badge** | [**UserBadge**](UserBadge.md) |  | 
**notes** | **List[str]** |  | [optional] 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.create_user_badge_response import CreateUserBadgeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserBadgeResponse from a JSON string
create_user_badge_response_instance = CreateUserBadgeResponse.from_json(json)
# print the JSON string representation of the object
print(CreateUserBadgeResponse.to_json())

# convert the object into a dict
create_user_badge_response_dict = create_user_badge_response_instance.to_dict()
# create an instance of CreateUserBadgeResponse from a dict
create_user_badge_response_from_dict = CreateUserBadgeResponse.from_dict(create_user_badge_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


