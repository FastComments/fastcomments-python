# GifSearchInternalError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**status** | [**APIStatus**](APIStatus.md) |  | 

## Example

```python
from client.models.gif_search_internal_error import GifSearchInternalError

# TODO update the JSON string below
json = "{}"
# create an instance of GifSearchInternalError from a JSON string
gif_search_internal_error_instance = GifSearchInternalError.from_json(json)
# print the JSON string representation of the object
print(GifSearchInternalError.to_json())

# convert the object into a dict
gif_search_internal_error_dict = gif_search_internal_error_instance.to_dict()
# create an instance of GifSearchInternalError from a dict
gif_search_internal_error_from_dict = GifSearchInternalError.from_dict(gif_search_internal_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


