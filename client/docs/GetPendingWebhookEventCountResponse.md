# GetPendingWebhookEventCountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**count** | **float** |  | 

## Example

```python
from client.models.get_pending_webhook_event_count_response import GetPendingWebhookEventCountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetPendingWebhookEventCountResponse from a JSON string
get_pending_webhook_event_count_response_instance = GetPendingWebhookEventCountResponse.from_json(json)
# print the JSON string representation of the object
print(GetPendingWebhookEventCountResponse.to_json())

# convert the object into a dict
get_pending_webhook_event_count_response_dict = get_pending_webhook_event_count_response_instance.to_dict()
# create an instance of GetPendingWebhookEventCountResponse from a dict
get_pending_webhook_event_count_response_from_dict = GetPendingWebhookEventCountResponse.from_dict(get_pending_webhook_event_count_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


