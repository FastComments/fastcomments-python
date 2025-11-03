# LiveEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**LiveEventType**](LiveEventType.md) |  | 
**timestamp** | **int** |  | [optional] 
**ts** | **int** |  | [optional] 
**broadcast_id** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**badges** | [**List[CommentUserBadgeInfo]**](CommentUserBadgeInfo.md) |  | [optional] 
**notification** | [**UserNotification**](UserNotification.md) |  | [optional] 
**vote** | [**PubSubVote**](PubSubVote.md) |  | [optional] 
**comment** | [**PubSubComment**](PubSubComment.md) |  | [optional] 
**feed_post** | [**FeedPost**](FeedPost.md) |  | [optional] 
**extra_info** | [**LiveEventExtraInfo**](LiveEventExtraInfo.md) |  | [optional] 
**config** | **object** |  | [optional] 
**is_closed** | **bool** |  | [optional] 
**uj** | **List[str]** |  | [optional] 
**ul** | **List[str]** |  | [optional] 
**changes** | **Dict[str, int]** |  | [optional] 

## Example

```python
from client.models.live_event import LiveEvent

# TODO update the JSON string below
json = "{}"
# create an instance of LiveEvent from a JSON string
live_event_instance = LiveEvent.from_json(json)
# print the JSON string representation of the object
print(LiveEvent.to_json())

# convert the object into a dict
live_event_dict = live_event_instance.to_dict()
# create an instance of LiveEvent from a dict
live_event_from_dict = LiveEvent.from_dict(live_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


