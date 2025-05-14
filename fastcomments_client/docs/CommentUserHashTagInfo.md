# CommentUserHashTagInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tag** | **str** |  | 
**url** | **str** |  | 
**retain** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.comment_user_hash_tag_info import CommentUserHashTagInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CommentUserHashTagInfo from a JSON string
comment_user_hash_tag_info_instance = CommentUserHashTagInfo.from_json(json)
# print the JSON string representation of the object
print(CommentUserHashTagInfo.to_json())

# convert the object into a dict
comment_user_hash_tag_info_dict = comment_user_hash_tag_info_instance.to_dict()
# create an instance of CommentUserHashTagInfo from a dict
comment_user_hash_tag_info_from_dict = CommentUserHashTagInfo.from_dict(comment_user_hash_tag_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


