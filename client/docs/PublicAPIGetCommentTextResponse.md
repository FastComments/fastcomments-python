# PublicAPIGetCommentTextResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**comment_text** | **str** |  | 
**sanitized_comment_text** | **str** |  | 

## Example

```python
from client.models.public_api_get_comment_text_response import PublicAPIGetCommentTextResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PublicAPIGetCommentTextResponse from a JSON string
public_api_get_comment_text_response_instance = PublicAPIGetCommentTextResponse.from_json(json)
# print the JSON string representation of the object
print(PublicAPIGetCommentTextResponse.to_json())

# convert the object into a dict
public_api_get_comment_text_response_dict = public_api_get_comment_text_response_instance.to_dict()
# create an instance of PublicAPIGetCommentTextResponse from a dict
public_api_get_comment_text_response_from_dict = PublicAPIGetCommentTextResponse.from_dict(public_api_get_comment_text_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


