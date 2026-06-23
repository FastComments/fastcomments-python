# UpdateUserNotificationPageSubscriptionStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**matched_count** | **int** |  | [optional] 
**modified_count** | **int** |  | [optional] 
**note** | **str** |  | [optional] 

## Example

```python
from client.models.update_user_notification_page_subscription_status_response import UpdateUserNotificationPageSubscriptionStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserNotificationPageSubscriptionStatusResponse from a JSON string
update_user_notification_page_subscription_status_response_instance = UpdateUserNotificationPageSubscriptionStatusResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateUserNotificationPageSubscriptionStatusResponse.to_json())

# convert the object into a dict
update_user_notification_page_subscription_status_response_dict = update_user_notification_page_subscription_status_response_instance.to_dict()
# create an instance of UpdateUserNotificationPageSubscriptionStatusResponse from a dict
update_user_notification_page_subscription_status_response_from_dict = UpdateUserNotificationPageSubscriptionStatusResponse.from_dict(update_user_notification_page_subscription_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


