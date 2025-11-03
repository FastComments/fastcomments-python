# DeletePageAPIResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**status** | **str** |  | 

## Example

```python
from generated.models.delete_page_api_response import DeletePageAPIResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeletePageAPIResponse from a JSON string
delete_page_api_response_instance = DeletePageAPIResponse.from_json(json)
# print the JSON string representation of the object
print(DeletePageAPIResponse.to_json())

# convert the object into a dict
delete_page_api_response_dict = delete_page_api_response_instance.to_dict()
# create an instance of DeletePageAPIResponse from a dict
delete_page_api_response_from_dict = DeletePageAPIResponse.from_dict(delete_page_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


