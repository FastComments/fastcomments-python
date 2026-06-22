# PostCommentsByIdsResponse


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
from client.models.post_comments_by_ids_response import PostCommentsByIdsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostCommentsByIdsResponse from a JSON string
post_comments_by_ids_response_instance = PostCommentsByIdsResponse.from_json(json)
# print the JSON string representation of the object
print(PostCommentsByIdsResponse.to_json())

# convert the object into a dict
post_comments_by_ids_response_dict = post_comments_by_ids_response_instance.to_dict()
# create an instance of PostCommentsByIdsResponse from a dict
post_comments_by_ids_response_from_dict = PostCommentsByIdsResponse.from_dict(post_comments_by_ids_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


