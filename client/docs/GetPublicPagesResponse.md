# GetPublicPagesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_cursor** | **str** |  | 
**pages** | [**List[PublicPage]**](PublicPage.md) |  | 
**status** | [**APIStatus**](APIStatus.md) |  | 

## Example

```python
from client.models.get_public_pages_response import GetPublicPagesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetPublicPagesResponse from a JSON string
get_public_pages_response_instance = GetPublicPagesResponse.from_json(json)
# print the JSON string representation of the object
print(GetPublicPagesResponse.to_json())

# convert the object into a dict
get_public_pages_response_dict = get_public_pages_response_instance.to_dict()
# create an instance of GetPublicPagesResponse from a dict
get_public_pages_response_from_dict = GetPublicPagesResponse.from_dict(get_public_pages_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


