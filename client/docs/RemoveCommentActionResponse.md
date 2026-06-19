# RemoveCommentActionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**action** | **str** |  | 

## Example

```python
from client.models.remove_comment_action_response import RemoveCommentActionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveCommentActionResponse from a JSON string
remove_comment_action_response_instance = RemoveCommentActionResponse.from_json(json)
# print the JSON string representation of the object
print(RemoveCommentActionResponse.to_json())

# convert the object into a dict
remove_comment_action_response_dict = remove_comment_action_response_instance.to_dict()
# create an instance of RemoveCommentActionResponse from a dict
remove_comment_action_response_from_dict = RemoveCommentActionResponse.from_dict(remove_comment_action_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


