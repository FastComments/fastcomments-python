# GetV2PageReactsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reacted_ids** | **List[str]** |  | [optional] 
**counts** | **Dict[str, float]** | Construct a type with a set of properties K of type T | [optional] 
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
from client.models.get_v2_page_reacts_response import GetV2PageReactsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetV2PageReactsResponse from a JSON string
get_v2_page_reacts_response_instance = GetV2PageReactsResponse.from_json(json)
# print the JSON string representation of the object
print(GetV2PageReactsResponse.to_json())

# convert the object into a dict
get_v2_page_reacts_response_dict = get_v2_page_reacts_response_instance.to_dict()
# create an instance of GetV2PageReactsResponse from a dict
get_v2_page_reacts_response_from_dict = GetV2PageReactsResponse.from_dict(get_v2_page_reacts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


