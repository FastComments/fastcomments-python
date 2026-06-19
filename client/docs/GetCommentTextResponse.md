# GetCommentTextResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** |  | [optional] 
**status** | [**APIStatus**](APIStatus.md) |  | 

## Example

```python
from client.models.get_comment_text_response import GetCommentTextResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCommentTextResponse from a JSON string
get_comment_text_response_instance = GetCommentTextResponse.from_json(json)
# print the JSON string representation of the object
print(GetCommentTextResponse.to_json())

# convert the object into a dict
get_comment_text_response_dict = get_comment_text_response_instance.to_dict()
# create an instance of GetCommentTextResponse from a dict
get_comment_text_response_from_dict = GetCommentTextResponse.from_dict(get_comment_text_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


