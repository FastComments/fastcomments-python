# DeletedCommentResultComment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_deleted** | **bool** |  | [optional] 
**comment_html** | **str** |  | 
**commenter_name** | **str** |  | 
**user_id** | **str** |  | [optional] 

## Example

```python
from client.models.deleted_comment_result_comment import DeletedCommentResultComment

# TODO update the JSON string below
json = "{}"
# create an instance of DeletedCommentResultComment from a JSON string
deleted_comment_result_comment_instance = DeletedCommentResultComment.from_json(json)
# print the JSON string representation of the object
print(DeletedCommentResultComment.to_json())

# convert the object into a dict
deleted_comment_result_comment_dict = deleted_comment_result_comment_instance.to_dict()
# create an instance of DeletedCommentResultComment from a dict
deleted_comment_result_comment_from_dict = DeletedCommentResultComment.from_dict(deleted_comment_result_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


