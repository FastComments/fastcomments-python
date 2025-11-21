# UnBlockCommentPublic200Response


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
from client.models.un_block_comment_public200_response import UnBlockCommentPublic200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UnBlockCommentPublic200Response from a JSON string
un_block_comment_public200_response_instance = UnBlockCommentPublic200Response.from_json(json)
# print the JSON string representation of the object
print(UnBlockCommentPublic200Response.to_json())

# convert the object into a dict
un_block_comment_public200_response_dict = un_block_comment_public200_response_instance.to_dict()
# create an instance of UnBlockCommentPublic200Response from a dict
un_block_comment_public200_response_from_dict = UnBlockCommentPublic200Response.from_dict(un_block_comment_public200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


