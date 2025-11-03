# PatchPageAPIResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**page** | [**APIPage**](APIPage.md) |  | [optional] 
**status** | **str** |  | 

## Example

```python
from client.models.patch_page_api_response import PatchPageAPIResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PatchPageAPIResponse from a JSON string
patch_page_api_response_instance = PatchPageAPIResponse.from_json(json)
# print the JSON string representation of the object
print(PatchPageAPIResponse.to_json())

# convert the object into a dict
patch_page_api_response_dict = patch_page_api_response_instance.to_dict()
# create an instance of PatchPageAPIResponse from a dict
patch_page_api_response_from_dict = PatchPageAPIResponse.from_dict(patch_page_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


