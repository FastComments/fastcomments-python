# GetPageByURLIdAPIResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**page** | [**APIPage**](APIPage.md) |  | [optional] 
**status** | **str** |  | 

## Example

```python
from client.models.get_page_by_urlid_api_response import GetPageByURLIdAPIResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetPageByURLIdAPIResponse from a JSON string
get_page_by_urlid_api_response_instance = GetPageByURLIdAPIResponse.from_json(json)
# print the JSON string representation of the object
print(GetPageByURLIdAPIResponse.to_json())

# convert the object into a dict
get_page_by_urlid_api_response_dict = get_page_by_urlid_api_response_instance.to_dict()
# create an instance of GetPageByURLIdAPIResponse from a dict
get_page_by_urlid_api_response_from_dict = GetPageByURLIdAPIResponse.from_dict(get_page_by_urlid_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


