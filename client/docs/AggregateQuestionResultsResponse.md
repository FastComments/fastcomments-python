# AggregateQuestionResultsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**data** | [**QuestionResultAggregationOverall**](QuestionResultAggregationOverall.md) |  | 

## Example

```python
from client.models.aggregate_question_results_response import AggregateQuestionResultsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AggregateQuestionResultsResponse from a JSON string
aggregate_question_results_response_instance = AggregateQuestionResultsResponse.from_json(json)
# print the JSON string representation of the object
print(AggregateQuestionResultsResponse.to_json())

# convert the object into a dict
aggregate_question_results_response_dict = aggregate_question_results_response_instance.to_dict()
# create an instance of AggregateQuestionResultsResponse from a dict
aggregate_question_results_response_from_dict = AggregateQuestionResultsResponse.from_dict(aggregate_question_results_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


