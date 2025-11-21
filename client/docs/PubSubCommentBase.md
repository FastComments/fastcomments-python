# PubSubCommentBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**user_id** | **str** |  | [optional] 
**url_id** | **str** |  | 
**commenter_name** | **str** |  | 
**commenter_link** | **str** |  | [optional] 
**comment_html** | **str** |  | 
**comment** | **str** |  | 
**parent_id** | **str** |  | [optional] 
**votes** | **int** |  | [optional] 
**votes_up** | **int** |  | [optional] 
**votes_down** | **int** |  | [optional] 
**verified** | **bool** |  | 
**avatar_src** | **str** |  | [optional] 
**has_images** | **bool** |  | [optional] 
**has_links** | **bool** |  | [optional] 
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
**flag_count** | **int** |  | [optional] 
**domain** | **str** |  | [optional] 
**url** | **str** |  | 
**page_title** | **str** |  | [optional] 
**expire_at** | **datetime** |  | [optional] 
**reviewed** | **bool** |  | [optional] 
**has_code** | **bool** |  | [optional] 
**approved** | **bool** |  | 
**locale** | **str** |  | 
**is_banned_user** | **bool** |  | [optional] 
**group_ids** | **List[str]** |  | [optional] 

## Example

```python
from client.models.pub_sub_comment_base import PubSubCommentBase

# TODO update the JSON string below
json = "{}"
# create an instance of PubSubCommentBase from a JSON string
pub_sub_comment_base_instance = PubSubCommentBase.from_json(json)
# print the JSON string representation of the object
print(PubSubCommentBase.to_json())

# convert the object into a dict
pub_sub_comment_base_dict = pub_sub_comment_base_instance.to_dict()
# create an instance of PubSubCommentBase from a dict
pub_sub_comment_base_from_dict = PubSubCommentBase.from_dict(pub_sub_comment_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


