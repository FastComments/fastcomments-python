# AggregationResponseStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_ms** | **float** |  | 
**scanned** | **float** |  | 

## Example

```python
from openapi_client.models.aggregation_response_stats import AggregationResponseStats

# TODO update the JSON string below
json = "{}"
# create an instance of AggregationResponseStats from a JSON string
aggregation_response_stats_instance = AggregationResponseStats.from_json(json)
# print the JSON string representation of the object
print(AggregationResponseStats.to_json())

# convert the object into a dict
aggregation_response_stats_dict = aggregation_response_stats_instance.to_dict()
# create an instance of AggregationResponseStats from a dict
aggregation_response_stats_from_dict = AggregationResponseStats.from_dict(aggregation_response_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


