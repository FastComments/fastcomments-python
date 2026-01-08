# GetQuestionResultResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**question_result** | [**QuestionResult**](QuestionResult.md) |  | 

## Example

```python
from client.models.get_question_result_response import GetQuestionResultResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetQuestionResultResponse from a JSON string
get_question_result_response_instance = GetQuestionResultResponse.from_json(json)
# print the JSON string representation of the object
print(GetQuestionResultResponse.to_json())

# convert the object into a dict
get_question_result_response_dict = get_question_result_response_instance.to_dict()
# create an instance of GetQuestionResultResponse from a dict
get_question_result_response_from_dict = GetQuestionResultResponse.from_dict(get_question_result_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


