# ResetUserNotificationsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ImportedAPIStatusSUCCESS**](ImportedAPIStatusSUCCESS.md) |  | 
**code** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.reset_user_notifications_response import ResetUserNotificationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResetUserNotificationsResponse from a JSON string
reset_user_notifications_response_instance = ResetUserNotificationsResponse.from_json(json)
# print the JSON string representation of the object
print(ResetUserNotificationsResponse.to_json())

# convert the object into a dict
reset_user_notifications_response_dict = reset_user_notifications_response_instance.to_dict()
# create an instance of ResetUserNotificationsResponse from a dict
reset_user_notifications_response_from_dict = ResetUserNotificationsResponse.from_dict(reset_user_notifications_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


