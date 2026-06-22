# GetCountsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **float** |  | 
**status** | [**APIStatus**](APIStatus.md) |  | 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.get_counts_response import GetCountsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCountsResponse from a JSON string
get_counts_response_instance = GetCountsResponse.from_json(json)
# print the JSON string representation of the object
print(GetCountsResponse.to_json())

# convert the object into a dict
get_counts_response_dict = get_counts_response_instance.to_dict()
# create an instance of GetCountsResponse from a dict
get_counts_response_from_dict = GetCountsResponse.from_dict(get_counts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


