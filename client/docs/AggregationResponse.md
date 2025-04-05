# AggregationResponse

The API response returns the aggregated data along with simple stats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**data** | [**List[AggregationItem]**](AggregationItem.md) |  | 
**stats** | [**AggregationResponseStats**](AggregationResponseStats.md) |  | [optional] 

## Example

```python
from openapi_client.models.aggregation_response import AggregationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AggregationResponse from a JSON string
aggregation_response_instance = AggregationResponse.from_json(json)
# print the JSON string representation of the object
print(AggregationResponse.to_json())

# convert the object into a dict
aggregation_response_dict = aggregation_response_instance.to_dict()
# create an instance of AggregationResponse from a dict
aggregation_response_from_dict = AggregationResponse.from_dict(aggregation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


