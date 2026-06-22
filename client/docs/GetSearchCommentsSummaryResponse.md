# GetSearchCommentsSummaryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment_count** | **int** |  | 
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
from client.models.get_search_comments_summary_response import GetSearchCommentsSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSearchCommentsSummaryResponse from a JSON string
get_search_comments_summary_response_instance = GetSearchCommentsSummaryResponse.from_json(json)
# print the JSON string representation of the object
print(GetSearchCommentsSummaryResponse.to_json())

# convert the object into a dict
get_search_comments_summary_response_dict = get_search_comments_summary_response_instance.to_dict()
# create an instance of GetSearchCommentsSummaryResponse from a dict
get_search_comments_summary_response_from_dict = GetSearchCommentsSummaryResponse.from_dict(get_search_comments_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


