# EventLogEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**created_at** | **datetime** |  | 
**tenant_id** | **str** |  | 
**url_id** | **str** |  | 
**broadcast_id** | **str** |  | 
**data** | **str** |  | 

## Example

```python
from client.models.event_log_entry import EventLogEntry

# TODO update the JSON string below
json = "{}"
# create an instance of EventLogEntry from a JSON string
event_log_entry_instance = EventLogEntry.from_json(json)
# print the JSON string representation of the object
print(EventLogEntry.to_json())

# convert the object into a dict
event_log_entry_dict = event_log_entry_instance.to_dict()
# create an instance of EventLogEntry from a dict
event_log_entry_from_dict = EventLogEntry.from_dict(event_log_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


