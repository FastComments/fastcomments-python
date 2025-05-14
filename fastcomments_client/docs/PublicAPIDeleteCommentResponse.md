# PublicAPIDeleteCommentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | [**PickFCommentIsDeletedOrCommentHTMLOrCommenterNameOrUserId**](PickFCommentIsDeletedOrCommentHTMLOrCommenterNameOrUserId.md) |  | [optional] 
**hard_removed** | **bool** |  | 
**status** | [**ImportedAPIStatusSUCCESS**](ImportedAPIStatusSUCCESS.md) |  | 

## Example

```python
from openapi_client.models.public_api_delete_comment_response import PublicAPIDeleteCommentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PublicAPIDeleteCommentResponse from a JSON string
public_api_delete_comment_response_instance = PublicAPIDeleteCommentResponse.from_json(json)
# print the JSON string representation of the object
print(PublicAPIDeleteCommentResponse.to_json())

# convert the object into a dict
public_api_delete_comment_response_dict = public_api_delete_comment_response_instance.to_dict()
# create an instance of PublicAPIDeleteCommentResponse from a dict
public_api_delete_comment_response_from_dict = PublicAPIDeleteCommentResponse.from_dict(public_api_delete_comment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


