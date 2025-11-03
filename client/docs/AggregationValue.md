# AggregationValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | **Dict[str, str]** | Construct a type with a set of properties K of type T | [optional] 
**string_value** | **str** |  | [optional] 
**numeric_value** | **float** |  | [optional] 
**distinct_count** | **int** |  | [optional] 
**distinct_counts** | **Dict[str, float]** | Construct a type with a set of properties K of type T | [optional] 

## Example

```python
from client.models.aggregation_value import AggregationValue

# TODO update the JSON string below
json = "{}"
# create an instance of AggregationValue from a JSON string
aggregation_value_instance = AggregationValue.from_json(json)
# print the JSON string representation of the object
print(AggregationValue.to_json())

# convert the object into a dict
aggregation_value_dict = aggregation_value_instance.to_dict()
# create an instance of AggregationValue from a dict
aggregation_value_from_dict = AggregationValue.from_dict(aggregation_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


