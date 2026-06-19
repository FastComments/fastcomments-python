# SetCommentTextResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_comment_text_html** | **str** |  | 
**status** | [**APIStatus**](APIStatus.md) |  | 

## Example

```python
from client.models.set_comment_text_response import SetCommentTextResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SetCommentTextResponse from a JSON string
set_comment_text_response_instance = SetCommentTextResponse.from_json(json)
# print the JSON string representation of the object
print(SetCommentTextResponse.to_json())

# convert the object into a dict
set_comment_text_response_dict = set_comment_text_response_instance.to_dict()
# create an instance of SetCommentTextResponse from a dict
set_comment_text_response_from_dict = SetCommentTextResponse.from_dict(set_comment_text_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


