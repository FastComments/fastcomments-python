# PendingCommentToSyncOutbound


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**comment_id** | **str** |  | 
**comment** | [**FComment**](FComment.md) |  | [optional] 
**external_id** | **str** |  | 
**created_at** | **datetime** |  | 
**tenant_id** | **str** |  | 
**attempt_count** | **float** |  | 
**next_attempt_at** | **datetime** |  | 
**event_type** | **float** |  | 
**type** | **float** |  | 
**domain** | **str** |  | 
**last_error** | **object** |  | 
**webhook_id** | **str** |  | [optional] 

## Example

```python
from client.models.pending_comment_to_sync_outbound import PendingCommentToSyncOutbound

# TODO update the JSON string below
json = "{}"
# create an instance of PendingCommentToSyncOutbound from a JSON string
pending_comment_to_sync_outbound_instance = PendingCommentToSyncOutbound.from_json(json)
# print the JSON string representation of the object
print(PendingCommentToSyncOutbound.to_json())

# convert the object into a dict
pending_comment_to_sync_outbound_dict = pending_comment_to_sync_outbound_instance.to_dict()
# create an instance of PendingCommentToSyncOutbound from a dict
pending_comment_to_sync_outbound_from_dict = PendingCommentToSyncOutbound.from_dict(pending_comment_to_sync_outbound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


