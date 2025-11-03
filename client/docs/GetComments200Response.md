# GetComments200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ImportedAPIStatusFAILED**](ImportedAPIStatusFAILED.md) |  | 
**comments** | [**List[PickFCommentAPICommentFieldsKeys]**](PickFCommentAPICommentFieldsKeys.md) |  | 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.get_comments200_response import GetComments200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetComments200Response from a JSON string
get_comments200_response_instance = GetComments200Response.from_json(json)
# print the JSON string representation of the object
print(GetComments200Response.to_json())

# convert the object into a dict
get_comments200_response_dict = get_comments200_response_instance.to_dict()
# create an instance of GetComments200Response from a dict
get_comments200_response_from_dict = GetComments200Response.from_dict(get_comments200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


