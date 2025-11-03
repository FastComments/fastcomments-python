# BulkAggregateQuestionResultsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregations** | [**List[BulkAggregateQuestionItem]**](BulkAggregateQuestionItem.md) |  | 

## Example

```python
from generated.models.bulk_aggregate_question_results_request import BulkAggregateQuestionResultsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkAggregateQuestionResultsRequest from a JSON string
bulk_aggregate_question_results_request_instance = BulkAggregateQuestionResultsRequest.from_json(json)
# print the JSON string representation of the object
print(BulkAggregateQuestionResultsRequest.to_json())

# convert the object into a dict
bulk_aggregate_question_results_request_dict = bulk_aggregate_question_results_request_instance.to_dict()
# create an instance of BulkAggregateQuestionResultsRequest from a dict
bulk_aggregate_question_results_request_from_dict = BulkAggregateQuestionResultsRequest.from_dict(bulk_aggregate_question_results_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


