# PublicAPISetCommentTextResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | [**SetCommentTextResult**](SetCommentTextResult.md) |  | 
**status** | [**APIStatus**](APIStatus.md) |  | 

## Example

```python
from client.models.public_api_set_comment_text_response import PublicAPISetCommentTextResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PublicAPISetCommentTextResponse from a JSON string
public_api_set_comment_text_response_instance = PublicAPISetCommentTextResponse.from_json(json)
# print the JSON string representation of the object
print(PublicAPISetCommentTextResponse.to_json())

# convert the object into a dict
public_api_set_comment_text_response_dict = public_api_set_comment_text_response_instance.to_dict()
# create an instance of PublicAPISetCommentTextResponse from a dict
public_api_set_comment_text_response_from_dict = PublicAPISetCommentTextResponse.from_dict(public_api_set_comment_text_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


