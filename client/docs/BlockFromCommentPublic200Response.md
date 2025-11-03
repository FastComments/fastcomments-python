# BlockFromCommentPublic200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ImportedAPIStatusFAILED**](ImportedAPIStatusFAILED.md) |  | 
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
from generated.models.block_from_comment_public200_response import BlockFromCommentPublic200Response

# TODO update the JSON string below
json = "{}"
# create an instance of BlockFromCommentPublic200Response from a JSON string
block_from_comment_public200_response_instance = BlockFromCommentPublic200Response.from_json(json)
# print the JSON string representation of the object
print(BlockFromCommentPublic200Response.to_json())

# convert the object into a dict
block_from_comment_public200_response_dict = block_from_comment_public200_response_instance.to_dict()
# create an instance of BlockFromCommentPublic200Response from a dict
block_from_comment_public200_response_from_dict = BlockFromCommentPublic200Response.from_dict(block_from_comment_public200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


