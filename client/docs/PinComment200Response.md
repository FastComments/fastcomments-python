# PinComment200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment_positions** | [**Dict[str, RecordStringBeforeStringOrNullAfterStringOrNullValue]**](RecordStringBeforeStringOrNullAfterStringOrNullValue.md) | Construct a type with a set of properties K of type T | 
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
from client.models.pin_comment200_response import PinComment200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PinComment200Response from a JSON string
pin_comment200_response_instance = PinComment200Response.from_json(json)
# print the JSON string representation of the object
print(PinComment200Response.to_json())

# convert the object into a dict
pin_comment200_response_dict = pin_comment200_response_instance.to_dict()
# create an instance of PinComment200Response from a dict
pin_comment200_response_from_dict = PinComment200Response.from_dict(pin_comment200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


