# DeleteNotificationCountResponse


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
from client.models.delete_notification_count_response import DeleteNotificationCountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteNotificationCountResponse from a JSON string
delete_notification_count_response_instance = DeleteNotificationCountResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteNotificationCountResponse.to_json())

# convert the object into a dict
delete_notification_count_response_dict = delete_notification_count_response_instance.to_dict()
# create an instance of DeleteNotificationCountResponse from a dict
delete_notification_count_response_from_dict = DeleteNotificationCountResponse.from_dict(delete_notification_count_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


