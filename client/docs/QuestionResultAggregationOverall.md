# QuestionResultAggregationOverall


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_by_date_bucket** | [**Dict[str, QuestionDatum]**](QuestionDatum.md) | Construct a type with a set of properties K of type T | [optional] 
**data_by_url_id** | [**Dict[str, QuestionDatum]**](QuestionDatum.md) | Construct a type with a set of properties K of type T | [optional] 
**counts_by_value** | **Dict[str, int]** |  | [optional] 
**total** | **int** |  | 
**average** | **float** |  | [optional] 
**created_at** | **datetime** |  | 

## Example

```python
from generated.models.question_result_aggregation_overall import QuestionResultAggregationOverall

# TODO update the JSON string below
json = "{}"
# create an instance of QuestionResultAggregationOverall from a JSON string
question_result_aggregation_overall_instance = QuestionResultAggregationOverall.from_json(json)
# print the JSON string representation of the object
print(QuestionResultAggregationOverall.to_json())

# convert the object into a dict
question_result_aggregation_overall_dict = question_result_aggregation_overall_instance.to_dict()
# create an instance of QuestionResultAggregationOverall from a dict
question_result_aggregation_overall_from_dict = QuestionResultAggregationOverall.from_dict(question_result_aggregation_overall_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


