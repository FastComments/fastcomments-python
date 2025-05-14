# DeleteCommentPublic200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | [**PickFCommentIsDeletedOrCommentHTMLOrCommenterNameOrUserId**](PickFCommentIsDeletedOrCommentHTMLOrCommenterNameOrUserId.md) |  | [optional] 
**hard_removed** | **bool** |  | 
**status** | [**ImportedAPIStatusFAILED**](ImportedAPIStatusFAILED.md) |  | 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **float** |  | [optional] 
**max_character_length** | **float** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from openapi_client.models.delete_comment_public200_response import DeleteCommentPublic200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteCommentPublic200Response from a JSON string
delete_comment_public200_response_instance = DeleteCommentPublic200Response.from_json(json)
# print the JSON string representation of the object
print(DeleteCommentPublic200Response.to_json())

# convert the object into a dict
delete_comment_public200_response_dict = delete_comment_public200_response_instance.to_dict()
# create an instance of DeleteCommentPublic200Response from a dict
delete_comment_public200_response_from_dict = DeleteCommentPublic200Response.from_dict(delete_comment_public200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


