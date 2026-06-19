# AggregationAPIError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**reason** | **str** |  | 
**code** | **str** |  | 
**valid_resource_names** | **List[str]** |  | [optional] 

## Example

```python
from client.models.aggregation_api_error import AggregationAPIError

# TODO update the JSON string below
json = "{}"
# create an instance of AggregationAPIError from a JSON string
aggregation_api_error_instance = AggregationAPIError.from_json(json)
# print the JSON string representation of the object
print(AggregationAPIError.to_json())

# convert the object into a dict
aggregation_api_error_dict = aggregation_api_error_instance.to_dict()
# create an instance of AggregationAPIError from a dict
aggregation_api_error_from_dict = AggregationAPIError.from_dict(aggregation_api_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


