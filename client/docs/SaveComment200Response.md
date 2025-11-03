# SaveComment200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ImportedAPIStatusFAILED**](ImportedAPIStatusFAILED.md) |  | 
**comment** | [**FComment**](FComment.md) |  | 
**user** | [**UserSessionInfo**](UserSessionInfo.md) |  | 
**module_data** | **Dict[str, object]** | Construct a type with a set of properties K of type T | [optional] 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from generated.models.save_comment200_response import SaveComment200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SaveComment200Response from a JSON string
save_comment200_response_instance = SaveComment200Response.from_json(json)
# print the JSON string representation of the object
print(SaveComment200Response.to_json())

# convert the object into a dict
save_comment200_response_dict = save_comment200_response_instance.to_dict()
# create an instance of SaveComment200Response from a dict
save_comment200_response_from_dict = SaveComment200Response.from_dict(save_comment200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


