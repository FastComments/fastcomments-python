# GetGlobalEventLogResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[EventLogEntry]**](EventLogEntry.md) |  | 
**status** | [**APIStatus**](APIStatus.md) |  | 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.get_global_event_log_response import GetGlobalEventLogResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetGlobalEventLogResponse from a JSON string
get_global_event_log_response_instance = GetGlobalEventLogResponse.from_json(json)
# print the JSON string representation of the object
print(GetGlobalEventLogResponse.to_json())

# convert the object into a dict
get_global_event_log_response_dict = get_global_event_log_response_instance.to_dict()
# create an instance of GetGlobalEventLogResponse from a dict
get_global_event_log_response_from_dict = GetGlobalEventLogResponse.from_dict(get_global_event_log_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


