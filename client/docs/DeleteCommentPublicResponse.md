# DeleteCommentPublicResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | [**DeletedCommentResultComment**](DeletedCommentResultComment.md) |  | [optional] 
**hard_removed** | **bool** |  | 
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
from client.models.delete_comment_public_response import DeleteCommentPublicResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteCommentPublicResponse from a JSON string
delete_comment_public_response_instance = DeleteCommentPublicResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteCommentPublicResponse.to_json())

# convert the object into a dict
delete_comment_public_response_dict = delete_comment_public_response_instance.to_dict()
# create an instance of DeleteCommentPublicResponse from a dict
delete_comment_public_response_from_dict = DeleteCommentPublicResponse.from_dict(delete_comment_public_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


