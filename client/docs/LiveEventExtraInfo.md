# LiveEventExtraInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment_positions** | [**Dict[str, RecordStringBeforeStringOrNullAfterStringOrNullValue]**](RecordStringBeforeStringOrNullAfterStringOrNullValue.md) | Construct a type with a set of properties K of type T | [optional] 

## Example

```python
from client.models.live_event_extra_info import LiveEventExtraInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LiveEventExtraInfo from a JSON string
live_event_extra_info_instance = LiveEventExtraInfo.from_json(json)
# print the JSON string representation of the object
print(LiveEventExtraInfo.to_json())

# convert the object into a dict
live_event_extra_info_dict = live_event_extra_info_instance.to_dict()
# create an instance of LiveEventExtraInfo from a dict
live_event_extra_info_from_dict = LiveEventExtraInfo.from_dict(live_event_extra_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


