# GifGetLargeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**src** | **str** |  | 
**status** | [**APIStatus**](APIStatus.md) |  | 

## Example

```python
from client.models.gif_get_large_response import GifGetLargeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GifGetLargeResponse from a JSON string
gif_get_large_response_instance = GifGetLargeResponse.from_json(json)
# print the JSON string representation of the object
print(GifGetLargeResponse.to_json())

# convert the object into a dict
gif_get_large_response_dict = gif_get_large_response_instance.to_dict()
# create an instance of GifGetLargeResponse from a dict
gif_get_large_response_from_dict = GifGetLargeResponse.from_dict(gif_get_large_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


