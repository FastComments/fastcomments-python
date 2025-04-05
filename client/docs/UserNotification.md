# UserNotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**user_id** | **str** |  | [optional] 
**anon_user_id** | **str** |  | [optional] 
**url_id** | **str** |  | 
**url** | **str** |  | 
**page_title** | **str** |  | [optional] 
**related_object_type** | **float** |  | 
**related_object_id** | **str** |  | 
**viewed** | **bool** |  | 
**is_unread_message** | **bool** |  | 
**sent** | **bool** |  | 
**created_at** | **datetime** |  | 
**type** | [**NotificationType**](NotificationType.md) |  | 
**from_comment_id** | **str** |  | [optional] 
**from_vote_id** | **str** |  | [optional] 
**from_user_name** | **str** |  | [optional] 
**from_user_id** | **str** |  | [optional] 
**from_user_avatar_src** | **str** |  | [optional] 
**opted_out** | **bool** |  | 

## Example

```python
from openapi_client.models.user_notification import UserNotification

# TODO update the JSON string below
json = "{}"
# create an instance of UserNotification from a JSON string
user_notification_instance = UserNotification.from_json(json)
# print the JSON string representation of the object
print(UserNotification.to_json())

# convert the object into a dict
user_notification_dict = user_notification_instance.to_dict()
# create an instance of UserNotification from a dict
user_notification_from_dict = UserNotification.from_dict(user_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


