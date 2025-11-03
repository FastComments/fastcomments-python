# FlagComment200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **int** |  | [optional] 
**status** | [**ImportedAPIStatusFAILED**](ImportedAPIStatusFAILED.md) |  | 
**code** | **str** |  | 
**reason** | **str** |  | 
**was_unapproved** | **bool** |  | [optional] 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from generated.models.flag_comment200_response import FlagComment200Response

# TODO update the JSON string below
json = "{}"
# create an instance of FlagComment200Response from a JSON string
flag_comment200_response_instance = FlagComment200Response.from_json(json)
# print the JSON string representation of the object
print(FlagComment200Response.to_json())

# convert the object into a dict
flag_comment200_response_dict = flag_comment200_response_instance.to_dict()
# create an instance of FlagComment200Response from a dict
flag_comment200_response_from_dict = FlagComment200Response.from_dict(flag_comment200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


