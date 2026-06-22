# GetGifLargeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**src** | **str** |  | 
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
from client.models.get_gif_large_response import GetGifLargeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetGifLargeResponse from a JSON string
get_gif_large_response_instance = GetGifLargeResponse.from_json(json)
# print the JSON string representation of the object
print(GetGifLargeResponse.to_json())

# convert the object into a dict
get_gif_large_response_dict = get_gif_large_response_instance.to_dict()
# create an instance of GetGifLargeResponse from a dict
get_gif_large_response_from_dict = GetGifLargeResponse.from_dict(get_gif_large_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


