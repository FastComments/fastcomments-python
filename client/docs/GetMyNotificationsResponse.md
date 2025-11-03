# GetMyNotificationsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**translations** | **Dict[str, str]** | Construct a type with a set of properties K of type T | [optional] 
**is_subscribed** | **bool** |  | 
**has_more** | **bool** |  | 
**notifications** | [**List[RenderableUserNotification]**](RenderableUserNotification.md) |  | 
**status** | [**ImportedAPIStatusSUCCESS**](ImportedAPIStatusSUCCESS.md) |  | 

## Example

```python
from generated.models.get_my_notifications_response import GetMyNotificationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetMyNotificationsResponse from a JSON string
get_my_notifications_response_instance = GetMyNotificationsResponse.from_json(json)
# print the JSON string representation of the object
print(GetMyNotificationsResponse.to_json())

# convert the object into a dict
get_my_notifications_response_dict = get_my_notifications_response_instance.to_dict()
# create an instance of GetMyNotificationsResponse from a dict
get_my_notifications_response_from_dict = GetMyNotificationsResponse.from_dict(get_my_notifications_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


