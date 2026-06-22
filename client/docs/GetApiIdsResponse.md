# GetApiIdsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** |  | 
**has_more** | **bool** |  | 
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
from client.models.get_api_ids_response import GetApiIdsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetApiIdsResponse from a JSON string
get_api_ids_response_instance = GetApiIdsResponse.from_json(json)
# print the JSON string representation of the object
print(GetApiIdsResponse.to_json())

# convert the object into a dict
get_api_ids_response_dict = get_api_ids_response_instance.to_dict()
# create an instance of GetApiIdsResponse from a dict
get_api_ids_response_from_dict = GetApiIdsResponse.from_dict(get_api_ids_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


