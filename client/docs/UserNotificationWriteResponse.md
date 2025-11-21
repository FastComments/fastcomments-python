# UserNotificationWriteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**matched_count** | **int** |  | 
**modified_count** | **int** |  | 

## Example

```python
from client.models.user_notification_write_response import UserNotificationWriteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserNotificationWriteResponse from a JSON string
user_notification_write_response_instance = UserNotificationWriteResponse.from_json(json)
# print the JSON string representation of the object
print(UserNotificationWriteResponse.to_json())

# convert the object into a dict
user_notification_write_response_dict = user_notification_write_response_instance.to_dict()
# create an instance of UserNotificationWriteResponse from a dict
user_notification_write_response_from_dict = UserNotificationWriteResponse.from_dict(user_notification_write_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


