# GifSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**images** | **List[List[GifSearchResponseImagesInnerInner]]** |  | 
**status** | [**APIStatus**](APIStatus.md) |  | 

## Example

```python
from client.models.gif_search_response import GifSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GifSearchResponse from a JSON string
gif_search_response_instance = GifSearchResponse.from_json(json)
# print the JSON string representation of the object
print(GifSearchResponse.to_json())

# convert the object into a dict
gif_search_response_dict = gif_search_response_instance.to_dict()
# create an instance of GifSearchResponse from a dict
gif_search_response_from_dict = GifSearchResponse.from_dict(gif_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


