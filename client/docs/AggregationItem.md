# AggregationItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | **Dict[str, str]** | Construct a type with a set of properties K of type T | [optional] 

## Example

```python
from openapi_client.models.aggregation_item import AggregationItem

# TODO update the JSON string below
json = "{}"
# create an instance of AggregationItem from a JSON string
aggregation_item_instance = AggregationItem.from_json(json)
# print the JSON string representation of the object
print(AggregationItem.to_json())

# convert the object into a dict
aggregation_item_dict = aggregation_item_instance.to_dict()
# create an instance of AggregationItem from a dict
aggregation_item_from_dict = AggregationItem.from_dict(aggregation_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


