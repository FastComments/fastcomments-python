# AggregateQuestionResults200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ImportedAPIStatusFAILED**](ImportedAPIStatusFAILED.md) |  | 
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
from generated.models.aggregate_question_results200_response import AggregateQuestionResults200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AggregateQuestionResults200Response from a JSON string
aggregate_question_results200_response_instance = AggregateQuestionResults200Response.from_json(json)
# print the JSON string representation of the object
print(AggregateQuestionResults200Response.to_json())

# convert the object into a dict
aggregate_question_results200_response_dict = aggregate_question_results200_response_instance.to_dict()
# create an instance of AggregateQuestionResults200Response from a dict
aggregate_question_results200_response_from_dict = AggregateQuestionResults200Response.from_dict(aggregate_question_results200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


