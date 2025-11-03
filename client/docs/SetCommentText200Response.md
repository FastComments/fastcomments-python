# SetCommentText200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | [**PickFCommentApprovedOrCommentHTML**](PickFCommentApprovedOrCommentHTML.md) |  | 
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
from generated.models.set_comment_text200_response import SetCommentText200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SetCommentText200Response from a JSON string
set_comment_text200_response_instance = SetCommentText200Response.from_json(json)
# print the JSON string representation of the object
print(SetCommentText200Response.to_json())

# convert the object into a dict
set_comment_text200_response_dict = set_comment_text200_response_instance.to_dict()
# create an instance of SetCommentText200Response from a dict
set_comment_text200_response_from_dict = SetCommentText200Response.from_dict(set_comment_text200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


