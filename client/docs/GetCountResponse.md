# GetCountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**count** | **float** |  | 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.get_count_response import GetCountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCountResponse from a JSON string
get_count_response_instance = GetCountResponse.from_json(json)
# print the JSON string representation of the object
print(GetCountResponse.to_json())

# convert the object into a dict
get_count_response_dict = get_count_response_instance.to_dict()
# create an instance of GetCountResponse from a dict
get_count_response_from_dict = GetCountResponse.from_dict(get_count_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


