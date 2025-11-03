# GetEventLog200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[EventLogEntry]**](EventLogEntry.md) |  | 
**status** | [**ImportedAPIStatusFAILED**](ImportedAPIStatusFAILED.md) |  | 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from generated.models.get_event_log200_response import GetEventLog200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetEventLog200Response from a JSON string
get_event_log200_response_instance = GetEventLog200Response.from_json(json)
# print the JSON string representation of the object
print(GetEventLog200Response.to_json())

# convert the object into a dict
get_event_log200_response_dict = get_event_log200_response_instance.to_dict()
# create an instance of GetEventLog200Response from a dict
get_event_log200_response_from_dict = GetEventLog200Response.from_dict(get_event_log200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


