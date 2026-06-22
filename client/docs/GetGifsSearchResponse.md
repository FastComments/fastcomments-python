# GetGifsSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**images** | **List[List[GifSearchResponseImagesInnerInner]]** |  | 
**status** | [**APIStatus**](APIStatus.md) |  | 
**code** | **str** |  | 

## Example

```python
from client.models.get_gifs_search_response import GetGifsSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetGifsSearchResponse from a JSON string
get_gifs_search_response_instance = GetGifsSearchResponse.from_json(json)
# print the JSON string representation of the object
print(GetGifsSearchResponse.to_json())

# convert the object into a dict
get_gifs_search_response_dict = get_gifs_search_response_instance.to_dict()
# create an instance of GetGifsSearchResponse from a dict
get_gifs_search_response_from_dict = GetGifsSearchResponse.from_dict(get_gifs_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


