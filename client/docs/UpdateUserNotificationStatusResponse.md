# UpdateUserNotificationStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**matched_count** | **int** |  | 
**modified_count** | **int** |  | 
**note** | **str** |  | 

## Example

```python
from client.models.update_user_notification_status_response import UpdateUserNotificationStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserNotificationStatusResponse from a JSON string
update_user_notification_status_response_instance = UpdateUserNotificationStatusResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateUserNotificationStatusResponse.to_json())

# convert the object into a dict
update_user_notification_status_response_dict = update_user_notification_status_response_instance.to_dict()
# create an instance of UpdateUserNotificationStatusResponse from a dict
update_user_notification_status_response_from_dict = UpdateUserNotificationStatusResponse.from_dict(update_user_notification_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


