# GetQuestionResultsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**question_results** | [**List[QuestionResult]**](QuestionResult.md) |  | 

## Example

```python
from client.models.get_question_results_response import GetQuestionResultsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetQuestionResultsResponse from a JSON string
get_question_results_response_instance = GetQuestionResultsResponse.from_json(json)
# print the JSON string representation of the object
print(GetQuestionResultsResponse.to_json())

# convert the object into a dict
get_question_results_response_dict = get_question_results_response_instance.to_dict()
# create an instance of GetQuestionResultsResponse from a dict
get_question_results_response_from_dict = GetQuestionResultsResponse.from_dict(get_question_results_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


