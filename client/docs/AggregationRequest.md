# AggregationRequest

The aggregation request accepts a resource, optional grouping keys, an array of operations, and an optional sort

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | [**List[QueryPredicate]**](QueryPredicate.md) |  | [optional] 
**resource_name** | **str** |  | 
**group_by** | **List[str]** |  | [optional] 
**operations** | [**List[AggregationOperation]**](AggregationOperation.md) |  | 
**sort** | [**AggregationRequestSort**](AggregationRequestSort.md) |  | [optional] 

## Example

```python
from generated.models.aggregation_request import AggregationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AggregationRequest from a JSON string
aggregation_request_instance = AggregationRequest.from_json(json)
# print the JSON string representation of the object
print(AggregationRequest.to_json())

# convert the object into a dict
aggregation_request_dict = aggregation_request_instance.to_dict()
# create an instance of AggregationRequest from a dict
aggregation_request_from_dict = AggregationRequest.from_dict(aggregation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


