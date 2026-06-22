# GetApiCommentsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**translations** | **object** |  | 
**comments** | [**List[ModerationAPIComment]**](ModerationAPIComment.md) |  | 
**moderation_filter** | [**ModerationFilter**](ModerationFilter.md) |  | [optional] 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.get_api_comments_response import GetApiCommentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetApiCommentsResponse from a JSON string
get_api_comments_response_instance = GetApiCommentsResponse.from_json(json)
# print the JSON string representation of the object
print(GetApiCommentsResponse.to_json())

# convert the object into a dict
get_api_comments_response_dict = get_api_comments_response_instance.to_dict()
# create an instance of GetApiCommentsResponse from a dict
get_api_comments_response_from_dict = GetApiCommentsResponse.from_dict(get_api_comments_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


