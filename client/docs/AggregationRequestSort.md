# AggregationRequestSort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dir** | **str** |  | 
**var_field** | **str** |  | 

## Example

```python
from client.models.aggregation_request_sort import AggregationRequestSort

# TODO update the JSON string below
json = "{}"
# create an instance of AggregationRequestSort from a JSON string
aggregation_request_sort_instance = AggregationRequestSort.from_json(json)
# print the JSON string representation of the object
print(AggregationRequestSort.to_json())

# convert the object into a dict
aggregation_request_sort_dict = aggregation_request_sort_instance.to_dict()
# create an instance of AggregationRequestSort from a dict
aggregation_request_sort_from_dict = AggregationRequestSort.from_dict(aggregation_request_sort_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


