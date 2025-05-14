# CommentUserMentionInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tag** | **str** |  | 
**raw_tag** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**sent** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.comment_user_mention_info import CommentUserMentionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CommentUserMentionInfo from a JSON string
comment_user_mention_info_instance = CommentUserMentionInfo.from_json(json)
# print the JSON string representation of the object
print(CommentUserMentionInfo.to_json())

# convert the object into a dict
comment_user_mention_info_dict = comment_user_mention_info_instance.to_dict()
# create an instance of CommentUserMentionInfo from a dict
comment_user_mention_info_from_dict = CommentUserMentionInfo.from_dict(comment_user_mention_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


