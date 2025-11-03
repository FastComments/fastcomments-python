# AggregationOperation

An operation that will be applied on a field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | The field to operate on | 
**op** | [**AggregationOpType**](AggregationOpType.md) |  | 
**alias** | **str** | Optional alias for the output; if not provided, a default alias is computed | [optional] 
**expand_array** | **bool** |  | [optional] 

## Example

```python
from generated.models.aggregation_operation import AggregationOperation

# TODO update the JSON string below
json = "{}"
# create an instance of AggregationOperation from a JSON string
aggregation_operation_instance = AggregationOperation.from_json(json)
# print the JSON string representation of the object
print(AggregationOperation.to_json())

# convert the object into a dict
aggregation_operation_dict = aggregation_operation_instance.to_dict()
# create an instance of AggregationOperation from a dict
aggregation_operation_from_dict = AggregationOperation.from_dict(aggregation_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


