# PublicCommentBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user_id** | **str** |  | [optional] 
**commenter_name** | **str** |  | 
**commenter_link** | **str** |  | [optional] 
**comment_html** | **str** |  | 
**parent_id** | **str** |  | [optional] 
**var_date** | **datetime** |  | 
**votes** | **int** |  | [optional] 
**votes_up** | **int** |  | [optional] 
**votes_down** | **int** |  | [optional] 
**verified** | **bool** |  | 
**avatar_src** | **str** |  | [optional] 
**has_images** | **bool** |  | [optional] 
**is_by_admin** | **bool** |  | [optional] 
**is_by_moderator** | **bool** |  | [optional] 
**is_pinned** | **bool** |  | [optional] 
**is_locked** | **bool** |  | [optional] 
**display_label** | **str** |  | [optional] 
**rating** | **float** |  | [optional] 
**badges** | [**List[CommentUserBadgeInfo]**](CommentUserBadgeInfo.md) |  | [optional] 
**view_count** | **int** |  | [optional] 
**is_deleted** | **bool** |  | [optional] 
**is_deleted_user** | **bool** |  | [optional] 
**is_spam** | **bool** |  | [optional] 
**anon_user_id** | **str** |  | [optional] 
**feedback_ids** | **List[str]** |  | [optional] 
**requires_verification** | **bool** |  | [optional] 
**edit_key** | **str** |  | [optional] 
**approved** | **bool** |  | [optional] 

## Example

```python
from client.models.public_comment_base import PublicCommentBase

# TODO update the JSON string below
json = "{}"
# create an instance of PublicCommentBase from a JSON string
public_comment_base_instance = PublicCommentBase.from_json(json)
# print the JSON string representation of the object
print(PublicCommentBase.to_json())

# convert the object into a dict
public_comment_base_dict = public_comment_base_instance.to_dict()
# create an instance of PublicCommentBase from a dict
public_comment_base_from_dict = PublicCommentBase.from_dict(public_comment_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


