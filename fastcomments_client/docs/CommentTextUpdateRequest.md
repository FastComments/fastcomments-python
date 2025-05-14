# CommentTextUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** |  | 
**mentions** | [**List[CommentUserMentionInfo]**](CommentUserMentionInfo.md) |  | [optional] 
**hash_tags** | [**List[CommentUserHashTagInfo]**](CommentUserHashTagInfo.md) |  | [optional] 

## Example

```python
from openapi_client.models.comment_text_update_request import CommentTextUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CommentTextUpdateRequest from a JSON string
comment_text_update_request_instance = CommentTextUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(CommentTextUpdateRequest.to_json())

# convert the object into a dict
comment_text_update_request_dict = comment_text_update_request_instance.to_dict()
# create an instance of CommentTextUpdateRequest from a dict
comment_text_update_request_from_dict = CommentTextUpdateRequest.from_dict(comment_text_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


