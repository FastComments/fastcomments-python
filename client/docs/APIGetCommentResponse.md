# APIGetCommentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**comment** | [**APIComment**](APIComment.md) |  | 

## Example

```python
from client.models.api_get_comment_response import APIGetCommentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of APIGetCommentResponse from a JSON string
api_get_comment_response_instance = APIGetCommentResponse.from_json(json)
# print the JSON string representation of the object
print(APIGetCommentResponse.to_json())

# convert the object into a dict
api_get_comment_response_dict = api_get_comment_response_instance.to_dict()
# create an instance of APIGetCommentResponse from a dict
api_get_comment_response_from_dict = APIGetCommentResponse.from_dict(api_get_comment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


