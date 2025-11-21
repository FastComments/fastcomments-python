# SetCommentTextResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approved** | **bool** |  | 
**comment_html** | **str** |  | 

## Example

```python
from client.models.set_comment_text_result import SetCommentTextResult

# TODO update the JSON string below
json = "{}"
# create an instance of SetCommentTextResult from a JSON string
set_comment_text_result_instance = SetCommentTextResult.from_json(json)
# print the JSON string representation of the object
print(SetCommentTextResult.to_json())

# convert the object into a dict
set_comment_text_result_dict = set_comment_text_result_instance.to_dict()
# create an instance of SetCommentTextResult from a dict
set_comment_text_result_from_dict = SetCommentTextResult.from_dict(set_comment_text_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


