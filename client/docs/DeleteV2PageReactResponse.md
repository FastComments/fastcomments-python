# DeleteV2PageReactResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**status** | [**APIStatus**](APIStatus.md) |  | 
**reason** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.delete_v2_page_react_response import DeleteV2PageReactResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteV2PageReactResponse from a JSON string
delete_v2_page_react_response_instance = DeleteV2PageReactResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteV2PageReactResponse.to_json())

# convert the object into a dict
delete_v2_page_react_response_dict = delete_v2_page_react_response_instance.to_dict()
# create an instance of DeleteV2PageReactResponse from a dict
delete_v2_page_react_response_from_dict = DeleteV2PageReactResponse.from_dict(delete_v2_page_react_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


