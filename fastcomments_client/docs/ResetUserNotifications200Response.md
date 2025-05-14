# ResetUserNotifications200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ImportedAPIStatusFAILED**](ImportedAPIStatusFAILED.md) |  | 
**code** | **str** |  | 
**reason** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **float** |  | [optional] 
**max_character_length** | **float** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from openapi_client.models.reset_user_notifications200_response import ResetUserNotifications200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ResetUserNotifications200Response from a JSON string
reset_user_notifications200_response_instance = ResetUserNotifications200Response.from_json(json)
# print the JSON string representation of the object
print(ResetUserNotifications200Response.to_json())

# convert the object into a dict
reset_user_notifications200_response_dict = reset_user_notifications200_response_instance.to_dict()
# create an instance of ResetUserNotifications200Response from a dict
reset_user_notifications200_response_from_dict = ResetUserNotifications200Response.from_dict(reset_user_notifications200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


