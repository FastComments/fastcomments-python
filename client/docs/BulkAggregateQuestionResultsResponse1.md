# BulkAggregateQuestionResultsResponse1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**data** | [**Dict[str, QuestionResultAggregationOverall]**](QuestionResultAggregationOverall.md) | Construct a type with a set of properties K of type T | 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.bulk_aggregate_question_results_response1 import BulkAggregateQuestionResultsResponse1

# TODO update the JSON string below
json = "{}"
# create an instance of BulkAggregateQuestionResultsResponse1 from a JSON string
bulk_aggregate_question_results_response1_instance = BulkAggregateQuestionResultsResponse1.from_json(json)
# print the JSON string representation of the object
print(BulkAggregateQuestionResultsResponse1.to_json())

# convert the object into a dict
bulk_aggregate_question_results_response1_dict = bulk_aggregate_question_results_response1_instance.to_dict()
# create an instance of BulkAggregateQuestionResultsResponse1 from a dict
bulk_aggregate_question_results_response1_from_dict = BulkAggregateQuestionResultsResponse1.from_dict(bulk_aggregate_question_results_response1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


