# BulkAggregateQuestionResultsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**data** | [**Dict[str, QuestionResultAggregationOverall]**](QuestionResultAggregationOverall.md) | Construct a type with a set of properties K of type T | 

## Example

```python
from client.models.bulk_aggregate_question_results_response import BulkAggregateQuestionResultsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkAggregateQuestionResultsResponse from a JSON string
bulk_aggregate_question_results_response_instance = BulkAggregateQuestionResultsResponse.from_json(json)
# print the JSON string representation of the object
print(BulkAggregateQuestionResultsResponse.to_json())

# convert the object into a dict
bulk_aggregate_question_results_response_dict = bulk_aggregate_question_results_response_instance.to_dict()
# create an instance of BulkAggregateQuestionResultsResponse from a dict
bulk_aggregate_question_results_response_from_dict = BulkAggregateQuestionResultsResponse.from_dict(bulk_aggregate_question_results_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


