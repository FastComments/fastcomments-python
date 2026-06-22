# UnBlockCommentPublicResponse


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
from client.models.un_block_comment_public_response import UnBlockCommentPublicResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UnBlockCommentPublicResponse from a JSON string
un_block_comment_public_response_instance = UnBlockCommentPublicResponse.from_json(json)
# print the JSON string representation of the object
print(UnBlockCommentPublicResponse.to_json())

# convert the object into a dict
un_block_comment_public_response_dict = un_block_comment_public_response_instance.to_dict()
# create an instance of UnBlockCommentPublicResponse from a dict
un_block_comment_public_response_from_dict = UnBlockCommentPublicResponse.from_dict(un_block_comment_public_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


