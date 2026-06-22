# GetSearchSuggestResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**pages** | [**List[ModerationPageSearchProjected]**](ModerationPageSearchProjected.md) |  | [optional] 
**users** | [**List[ModerationUserSearchProjected]**](ModerationUserSearchProjected.md) |  | [optional] 
**code** | **str** |  | 
**reason** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.get_search_suggest_response import GetSearchSuggestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSearchSuggestResponse from a JSON string
get_search_suggest_response_instance = GetSearchSuggestResponse.from_json(json)
# print the JSON string representation of the object
print(GetSearchSuggestResponse.to_json())

# convert the object into a dict
get_search_suggest_response_dict = get_search_suggest_response_instance.to_dict()
# create an instance of GetSearchSuggestResponse from a dict
get_search_suggest_response_from_dict = GetSearchSuggestResponse.from_dict(get_search_suggest_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


