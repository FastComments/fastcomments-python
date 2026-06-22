# BlockUserFromCommentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**comment_statuses** | **Dict[str, bool]** | Construct a type with a set of properties K of type T | 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.block_user_from_comment_response import BlockUserFromCommentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BlockUserFromCommentResponse from a JSON string
block_user_from_comment_response_instance = BlockUserFromCommentResponse.from_json(json)
# print the JSON string representation of the object
print(BlockUserFromCommentResponse.to_json())

# convert the object into a dict
block_user_from_comment_response_dict = block_user_from_comment_response_instance.to_dict()
# create an instance of BlockUserFromCommentResponse from a dict
block_user_from_comment_response_from_dict = BlockUserFromCommentResponse.from_dict(block_user_from_comment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


