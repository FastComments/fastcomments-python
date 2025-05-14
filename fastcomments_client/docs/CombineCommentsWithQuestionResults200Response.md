# CombineCommentsWithQuestionResults200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ImportedAPIStatusFAILED**](ImportedAPIStatusFAILED.md) |  | 
**data** | [**FindCommentsByRangeResponse**](FindCommentsByRangeResponse.md) |  | 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **float** |  | [optional] 
**max_character_length** | **float** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from openapi_client.models.combine_comments_with_question_results200_response import CombineCommentsWithQuestionResults200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CombineCommentsWithQuestionResults200Response from a JSON string
combine_comments_with_question_results200_response_instance = CombineCommentsWithQuestionResults200Response.from_json(json)
# print the JSON string representation of the object
print(CombineCommentsWithQuestionResults200Response.to_json())

# convert the object into a dict
combine_comments_with_question_results200_response_dict = combine_comments_with_question_results200_response_instance.to_dict()
# create an instance of CombineCommentsWithQuestionResults200Response from a dict
combine_comments_with_question_results200_response_from_dict = CombineCommentsWithQuestionResults200Response.from_dict(combine_comments_with_question_results200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


