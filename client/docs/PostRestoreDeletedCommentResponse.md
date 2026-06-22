# PostRestoreDeletedCommentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
from client.models.post_restore_deleted_comment_response import PostRestoreDeletedCommentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostRestoreDeletedCommentResponse from a JSON string
post_restore_deleted_comment_response_instance = PostRestoreDeletedCommentResponse.from_json(json)
# print the JSON string representation of the object
print(PostRestoreDeletedCommentResponse.to_json())

# convert the object into a dict
post_restore_deleted_comment_response_dict = post_restore_deleted_comment_response_instance.to_dict()
# create an instance of PostRestoreDeletedCommentResponse from a dict
post_restore_deleted_comment_response_from_dict = PostRestoreDeletedCommentResponse.from_dict(post_restore_deleted_comment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


