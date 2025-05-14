# RenderableUserNotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**url_id** | **str** |  | 
**url** | **str** |  | 
**page_title** | **str** |  | [optional] 
**related_object_type** | **float** |  | 
**related_object_id** | **str** |  | 
**viewed** | **bool** |  | 
**sent** | **bool** |  | 
**created_at** | **datetime** |  | 
**type** | [**NotificationType**](NotificationType.md) |  | 
**from_comment_id** | **str** |  | [optional] 
**from_user_name** | **str** |  | 
**from_user_id** | **str** |  | 
**from_user_avatar_src** | **str** |  | [optional] 
**opted_out** | **bool** |  | 
**conversation_id** | **str** |  | [optional] 
**context_html** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.renderable_user_notification import RenderableUserNotification

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


