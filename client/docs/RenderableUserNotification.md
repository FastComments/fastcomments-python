# RenderableUserNotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation_id** | **str** |  | [optional] 
**context_html** | **str** |  | [optional] 
**from_user_names** | **List[str]** |  | [optional] 
**from_user_ids** | **List[str]** |  | [optional] 
**related_ids** | **List[str]** |  | [optional] 
**count** | **int** |  | [optional] 
**opted_out** | **bool** |  | 
**from_user_avatar_src** | **str** |  | [optional] 
**from_user_id** | **str** |  | [optional] 
**from_user_name** | **str** |  | [optional] 
**from_comment_id** | **str** |  | [optional] 
**type** | [**NotificationType**](NotificationType.md) |  | 
**created_at** | **str** |  | 
**sent** | **str** |  | 
**viewed** | **str** |  | 
**related_object_id** | **str** |  | 
**related_object_type** | [**NotificationObjectType**](NotificationObjectType.md) |  | 
**page_title** | **str** |  | [optional] 
**url** | **str** |  | 
**url_id** | **str** |  | 
**id** | **str** |  | 

## Example

```python
from generated.models.renderable_user_notification import RenderableUserNotification

# TODO update the JSON string below
json = "{}"
# create an instance of RenderableUserNotification from a JSON string
renderable_user_notification_instance = RenderableUserNotification.from_json(json)
# print the JSON string representation of the object
print(RenderableUserNotification.to_json())

# convert the object into a dict
renderable_user_notification_dict = renderable_user_notification_instance.to_dict()
# create an instance of RenderableUserNotification from a dict
renderable_user_notification_from_dict = RenderableUserNotification.from_dict(renderable_user_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


