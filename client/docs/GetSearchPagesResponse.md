# GetSearchPagesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pages** | [**List[ModerationPageSearchProjected]**](ModerationPageSearchProjected.md) |  | 
**status** | [**APIStatus**](APIStatus.md) |  | 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.get_search_pages_response import GetSearchPagesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSearchPagesResponse from a JSON string
get_search_pages_response_instance = GetSearchPagesResponse.from_json(json)
# print the JSON string representation of the object
print(GetSearchPagesResponse.to_json())

# convert the object into a dict
get_search_pages_response_dict = get_search_pages_response_instance.to_dict()
# create an instance of GetSearchPagesResponse from a dict
get_search_pages_response_from_dict = GetSearchPagesResponse.from_dict(get_search_pages_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


