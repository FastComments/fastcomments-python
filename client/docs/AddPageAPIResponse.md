# AddPageAPIResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**page** | [**APIPage**](APIPage.md) |  | [optional] 
**status** | **str** |  | 

## Example

```python
from client.models.add_page_api_response import AddPageAPIResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddPageAPIResponse from a JSON string
add_page_api_response_instance = AddPageAPIResponse.from_json(json)
# print the JSON string representation of the object
print(AddPageAPIResponse.to_json())

# convert the object into a dict
add_page_api_response_dict = add_page_api_response_instance.to_dict()
# create an instance of AddPageAPIResponse from a dict
add_page_api_response_from_dict = AddPageAPIResponse.from_dict(add_page_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


