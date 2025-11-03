# UpdateUserBadge200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ImportedAPIStatusFAILED**](ImportedAPIStatusFAILED.md) |  | 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from generated.models.update_user_badge200_response import UpdateUserBadge200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserBadge200Response from a JSON string
update_user_badge200_response_instance = UpdateUserBadge200Response.from_json(json)
# print the JSON string representation of the object
print(UpdateUserBadge200Response.to_json())

# convert the object into a dict
update_user_badge200_response_dict = update_user_badge200_response_instance.to_dict()
# create an instance of UpdateUserBadge200Response from a dict
update_user_badge200_response_from_dict = UpdateUserBadge200Response.from_dict(update_user_badge200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


