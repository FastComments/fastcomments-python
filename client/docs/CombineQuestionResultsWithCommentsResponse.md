# CombineQuestionResultsWithCommentsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**data** | [**FindCommentsByRangeResponse**](FindCommentsByRangeResponse.md) |  | 

## Example

```python
from generated.models.combine_question_results_with_comments_response import CombineQuestionResultsWithCommentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CombineQuestionResultsWithCommentsResponse from a JSON string
combine_question_results_with_comments_response_instance = CombineQuestionResultsWithCommentsResponse.from_json(json)
# print the JSON string representation of the object
print(CombineQuestionResultsWithCommentsResponse.to_json())

# convert the object into a dict
combine_question_results_with_comments_response_dict = combine_question_results_with_comments_response_instance.to_dict()
# create an instance of CombineQuestionResultsWithCommentsResponse from a dict
combine_question_results_with_comments_response_from_dict = CombineQuestionResultsWithCommentsResponse.from_dict(combine_question_results_with_comments_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


