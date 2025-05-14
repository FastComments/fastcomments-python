# GetEventLogResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[EventLogEntry]**](EventLogEntry.md) |  | 
**status** | [**ImportedAPIStatusSUCCESS**](ImportedAPIStatusSUCCESS.md) |  | 

## Example

```python
from openapi_client.models.get_event_log_response import GetEventLogResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetEventLogResponse from a JSON string
get_event_log_response_instance = GetEventLogResponse.from_json(json)
# print the JSON string representation of the object
print(GetEventLogResponse.to_json())

# convert the object into a dict
get_event_log_response_dict = get_event_log_response_instance.to_dict()
# create an instance of GetEventLogResponse from a dict
get_event_log_response_from_dict = GetEventLogResponse.from_dict(get_event_log_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


