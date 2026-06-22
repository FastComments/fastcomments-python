# ResetUserNotificationsResponse1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**code** | **str** |  | 
**reason** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.reset_user_notifications_response1 import ResetUserNotificationsResponse1

# TODO update the JSON string below
json = "{}"
# create an instance of ResetUserNotificationsResponse1 from a JSON string
reset_user_notifications_response1_instance = ResetUserNotificationsResponse1.from_json(json)
# print the JSON string representation of the object
print(ResetUserNotificationsResponse1.to_json())

# convert the object into a dict
reset_user_notifications_response1_dict = reset_user_notifications_response1_instance.to_dict()
# create an instance of ResetUserNotificationsResponse1 from a dict
reset_user_notifications_response1_from_dict = ResetUserNotificationsResponse1.from_dict(reset_user_notifications_response1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


