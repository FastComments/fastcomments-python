# GetPagesAPIResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**pages** | [**List[APIPage]**](APIPage.md) |  | [optional] 
**status** | **str** |  | 

## Example

```python
from generated.models.get_pages_api_response import GetPagesAPIResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetPagesAPIResponse from a JSON string
get_pages_api_response_instance = GetPagesAPIResponse.from_json(json)
# print the JSON string representation of the object
print(GetPagesAPIResponse.to_json())

# convert the object into a dict
get_pages_api_response_dict = get_pages_api_response_instance.to_dict()
# create an instance of GetPagesAPIResponse from a dict
get_pages_api_response_from_dict = GetPagesAPIResponse.from_dict(get_pages_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


