# BulkAggregateQuestionResults200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ImportedAPIStatusFAILED**](ImportedAPIStatusFAILED.md) |  | 
**data** | [**Dict[str, QuestionResultAggregationOverall]**](QuestionResultAggregationOverall.md) | Construct a type with a set of properties K of type T | 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **float** |  | [optional] 
**max_character_length** | **float** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from openapi_client.models.bulk_aggregate_question_results200_response import BulkAggregateQuestionResults200Response

# TODO update the JSON string below
json = "{}"
# create an instance of BulkAggregateQuestionResults200Response from a JSON string
bulk_aggregate_question_results200_response_instance = BulkAggregateQuestionResults200Response.from_json(json)
# print the JSON string representation of the object
print(BulkAggregateQuestionResults200Response.to_json())

# convert the object into a dict
bulk_aggregate_question_results200_response_dict = bulk_aggregate_question_results200_response_instance.to_dict()
# create an instance of BulkAggregateQuestionResults200Response from a dict
bulk_aggregate_question_results200_response_from_dict = BulkAggregateQuestionResults200Response.from_dict(bulk_aggregate_question_results200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


