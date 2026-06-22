# AggregateQuestionResultsResponse1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**data** | [**QuestionResultAggregationOverall**](QuestionResultAggregationOverall.md) |  | 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.aggregate_question_results_response1 import AggregateQuestionResultsResponse1

# TODO update the JSON string below
json = "{}"
# create an instance of AggregateQuestionResultsResponse1 from a JSON string
aggregate_question_results_response1_instance = AggregateQuestionResultsResponse1.from_json(json)
# print the JSON string representation of the object
print(AggregateQuestionResultsResponse1.to_json())

# convert the object into a dict
aggregate_question_results_response1_dict = aggregate_question_results_response1_instance.to_dict()
# create an instance of AggregateQuestionResultsResponse1 from a dict
aggregate_question_results_response1_from_dict = AggregateQuestionResultsResponse1.from_dict(aggregate_question_results_response1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


