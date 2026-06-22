# GetCommentChildrenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comments** | [**List[ModerationAPIComment]**](ModerationAPIComment.md) |  | 
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
from client.models.get_comment_children_response import GetCommentChildrenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCommentChildrenResponse from a JSON string
get_comment_children_response_instance = GetCommentChildrenResponse.from_json(json)
# print the JSON string representation of the object
print(GetCommentChildrenResponse.to_json())

# convert the object into a dict
get_comment_children_response_dict = get_comment_children_response_instance.to_dict()
# create an instance of GetCommentChildrenResponse from a dict
get_comment_children_response_from_dict = GetCommentChildrenResponse.from_dict(get_comment_children_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


