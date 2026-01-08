# UserNotificationCount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**count** | **float** |  | 
**created_at** | **datetime** |  | 
**expire_at** | **datetime** |  | 

## Example

```python
from client.models.user_notification_count import UserNotificationCount

# TODO update the JSON string below
json = "{}"
# create an instance of UserNotificationCount from a JSON string
user_notification_count_instance = UserNotificationCount.from_json(json)
# print the JSON string representation of the object
print(UserNotificationCount.to_json())

# convert the object into a dict
user_notification_count_dict = user_notification_count_instance.to_dict()
# create an instance of UserNotificationCount from a dict
user_notification_count_from_dict = UserNotificationCount.from_dict(user_notification_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


