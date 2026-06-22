# CreateV1PageReactResponse


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
from client.models.create_v1_page_react_response import CreateV1PageReactResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateV1PageReactResponse from a JSON string
create_v1_page_react_response_instance = CreateV1PageReactResponse.from_json(json)
# print the JSON string representation of the object
print(CreateV1PageReactResponse.to_json())

# convert the object into a dict
create_v1_page_react_response_dict = create_v1_page_react_response_instance.to_dict()
# create an instance of CreateV1PageReactResponse from a dict
create_v1_page_react_response_from_dict = CreateV1PageReactResponse.from_dict(create_v1_page_react_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


