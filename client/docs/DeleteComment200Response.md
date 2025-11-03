# DeleteComment200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**DeleteCommentAction**](DeleteCommentAction.md) |  | 
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
from generated.models.delete_comment200_response import DeleteComment200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteComment200Response from a JSON string
delete_comment200_response_instance = DeleteComment200Response.from_json(json)
# print the JSON string representation of the object
print(DeleteComment200Response.to_json())

# convert the object into a dict
delete_comment200_response_dict = delete_comment200_response_instance.to_dict()
# create an instance of DeleteComment200Response from a dict
delete_comment200_response_from_dict = DeleteComment200Response.from_dict(delete_comment200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


