# GetUserNotificationCountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**count** | **int** |  | 

## Example

```python
from client.models.get_user_notification_count_response import GetUserNotificationCountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserNotificationCountResponse from a JSON string
get_user_notification_count_response_instance = GetUserNotificationCountResponse.from_json(json)
# print the JSON string representation of the object
print(GetUserNotificationCountResponse.to_json())

# convert the object into a dict
get_user_notification_count_response_dict = get_user_notification_count_response_instance.to_dict()
# create an instance of GetUserNotificationCountResponse from a dict
get_user_notification_count_response_from_dict = GetUserNotificationCountResponse.from_dict(get_user_notification_count_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


