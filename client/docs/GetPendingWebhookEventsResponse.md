# GetPendingWebhookEventsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**pending_webhook_events** | [**List[PendingCommentToSyncOutbound]**](PendingCommentToSyncOutbound.md) |  | 

## Example

```python
from client.models.get_pending_webhook_events_response import GetPendingWebhookEventsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetPendingWebhookEventsResponse from a JSON string
get_pending_webhook_events_response_instance = GetPendingWebhookEventsResponse.from_json(json)
# print the JSON string representation of the object
print(GetPendingWebhookEventsResponse.to_json())

# convert the object into a dict
get_pending_webhook_events_response_dict = get_pending_webhook_events_response_instance.to_dict()
# create an instance of GetPendingWebhookEventsResponse from a dict
get_pending_webhook_events_response_from_dict = GetPendingWebhookEventsResponse.from_dict(get_pending_webhook_events_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


