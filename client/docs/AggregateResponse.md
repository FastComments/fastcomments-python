# AggregateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**data** | [**List[AggregationItem]**](AggregationItem.md) |  | [optional] 
**stats** | [**AggregationResponseStats**](AggregationResponseStats.md) |  | [optional] 
**reason** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**valid_resource_names** | **List[str]** |  | [optional] 

## Example

```python
from client.models.aggregate_response import AggregateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AggregateResponse from a JSON string
aggregate_response_instance = AggregateResponse.from_json(json)
# print the JSON string representation of the object
print(AggregateResponse.to_json())

# convert the object into a dict
aggregate_response_dict = aggregate_response_instance.to_dict()
# create an instance of AggregateResponse from a dict
aggregate_response_from_dict = AggregateResponse.from_dict(aggregate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


