# CreateQuestionResultResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**question_result** | [**QuestionResult**](QuestionResult.md) |  | 

## Example

```python
from client.models.create_question_result_response import CreateQuestionResultResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateQuestionResultResponse from a JSON string
create_question_result_response_instance = CreateQuestionResultResponse.from_json(json)
# print the JSON string representation of the object
print(CreateQuestionResultResponse.to_json())

# convert the object into a dict
create_question_result_response_dict = create_question_result_response_instance.to_dict()
# create an instance of CreateQuestionResultResponse from a dict
create_question_result_response_from_dict = CreateQuestionResultResponse.from_dict(create_question_result_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


