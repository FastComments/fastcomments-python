# ModerationAPIComment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_local_deleted** | **bool** |  | [optional] 
**reply_count** | **float** |  | [optional] 
**feedback_results** | **List[str]** |  | [optional] 
**is_voted_up** | **bool** |  | [optional] 
**is_voted_down** | **bool** |  | [optional] 
**my_vote_id** | **str** |  | [optional] 
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**url_id** | **str** |  | 
**url** | **str** |  | 
**page_title** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**anon_user_id** | **str** |  | [optional] 
**commenter_name** | **str** |  | 
**commenter_link** | **str** |  | [optional] 
**comment_html** | **str** |  | 
**parent_id** | **str** |  | [optional] 
**var_date** | **datetime** |  | 
**local_date_string** | **str** |  | [optional] 
**votes** | **float** |  | [optional] 
**votes_up** | **float** |  | [optional] 
**votes_down** | **float** |  | [optional] 
**expire_at** | **datetime** |  | [optional] 
**reviewed** | **bool** |  | [optional] 
**avatar_src** | **str** |  | [optional] 
**is_spam** | **bool** |  | [optional] 
**perm_not_spam** | **bool** |  | [optional] 
**has_links** | **bool** |  | [optional] 
**has_code** | **bool** |  | [optional] 
**approved** | **bool** |  | 
**locale** | **str** |  | 
**is_banned_user** | **bool** |  | [optional] 
**is_by_admin** | **bool** |  | [optional] 
**is_by_moderator** | **bool** |  | [optional] 
**is_pinned** | **bool** |  | [optional] 
**is_locked** | **bool** |  | [optional] 
**flag_count** | **float** |  | [optional] 
**display_label** | **str** |  | [optional] 
**badges** | [**List[CommentUserBadgeInfo]**](CommentUserBadgeInfo.md) |  | [optional] 
**verified** | **bool** |  | 
**feedback_ids** | **List[str]** |  | [optional] 
**is_deleted** | **bool** |  | [optional] 

## Example

```python
from client.models.moderation_api_comment import ModerationAPIComment

# TODO update the JSON string below
json = "{}"
# create an instance of ModerationAPIComment from a JSON string
moderation_api_comment_instance = ModerationAPIComment.from_json(json)
# print the JSON string representation of the object
print(ModerationAPIComment.to_json())

# convert the object into a dict
moderation_api_comment_dict = moderation_api_comment_instance.to_dict()
# create an instance of ModerationAPIComment from a dict
moderation_api_comment_from_dict = ModerationAPIComment.from_dict(moderation_api_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


