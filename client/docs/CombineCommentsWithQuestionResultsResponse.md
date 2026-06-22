# CombineCommentsWithQuestionResultsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**data** | [**FindCommentsByRangeResponse**](FindCommentsByRangeResponse.md) |  | 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.combine_comments_with_question_results_response import CombineCommentsWithQuestionResultsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CombineCommentsWithQuestionResultsResponse from a JSON string
combine_comments_with_question_results_response_instance = CombineCommentsWithQuestionResultsResponse.from_json(json)
# print the JSON string representation of the object
print(CombineCommentsWithQuestionResultsResponse.to_json())

# convert the object into a dict
combine_comments_with_question_results_response_dict = combine_comments_with_question_results_response_instance.to_dict()
# create an instance of CombineCommentsWithQuestionResultsResponse from a dict
combine_comments_with_question_results_response_from_dict = CombineCommentsWithQuestionResultsResponse.from_dict(combine_comments_with_question_results_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


