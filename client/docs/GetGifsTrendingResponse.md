# GetGifsTrendingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**images** | **List[List[GifSearchResponseImagesInnerInner]]** |  | 
**status** | [**APIStatus**](APIStatus.md) |  | 
**code** | **str** |  | 

## Example

```python
from client.models.get_gifs_trending_response import GetGifsTrendingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetGifsTrendingResponse from a JSON string
get_gifs_trending_response_instance = GetGifsTrendingResponse.from_json(json)
# print the JSON string representation of the object
print(GetGifsTrendingResponse.to_json())

# convert the object into a dict
get_gifs_trending_response_dict = get_gifs_trending_response_instance.to_dict()
# create an instance of GetGifsTrendingResponse from a dict
get_gifs_trending_response_from_dict = GetGifsTrendingResponse.from_dict(get_gifs_trending_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


