# PubSubComment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | 
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**url_id** | **str** |  | 
**url** | **str** |  | 
**page_title** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**anon_user_id** | **str** |  | [optional] 
**commenter_name** | **str** |  | 
**commenter_link** | **str** |  | [optional] 
**comment** | **str** |  | 
**comment_html** | **str** |  | 
**parent_id** | **str** |  | [optional] 
**votes** | **int** |  | [optional] 
**votes_up** | **int** |  | [optional] 
**votes_down** | **int** |  | [optional] 
**expire_at** | **datetime** |  | [optional] 
**verified** | **bool** |  | 
**reviewed** | **bool** |  | [optional] 
**avatar_src** | **str** |  | [optional] 
**is_spam** | **bool** |  | [optional] 
**has_images** | **bool** |  | [optional] 
**has_links** | **bool** |  | [optional] 
**has_code** | **bool** |  | [optional] 
**approved** | **bool** |  | 
**locale** | **str** |  | 
**is_deleted** | **bool** |  | [optional] 
**is_deleted_user** | **bool** |  | [optional] 
**is_banned_user** | **bool** |  | [optional] 
**is_by_admin** | **bool** |  | [optional] 
**is_by_moderator** | **bool** |  | [optional] 
**is_pinned** | **bool** |  | [optional] 
**is_locked** | **bool** |  | [optional] 
**flag_count** | **int** |  | [optional] 
**rating** | **float** |  | [optional] 
**display_label** | **str** |  | [optional] 
**badges** | [**List[CommentUserBadgeInfo]**](CommentUserBadgeInfo.md) |  | [optional] 
**domain** | **str** |  | [optional] 
**feedback_ids** | **List[str]** |  | [optional] 
**group_ids** | **List[str]** |  | [optional] 
**view_count** | **int** |  | [optional] 
**is_live** | **bool** |  | [optional] 
**hidden** | **bool** |  | [optional] 

## Example

```python
from client.models.pub_sub_comment import PubSubComment

# TODO update the JSON string below
json = "{}"
# create an instance of PubSubComment from a JSON string
pub_sub_comment_instance = PubSubComment.from_json(json)
# print the JSON string representation of the object
print(PubSubComment.to_json())

# convert the object into a dict
pub_sub_comment_dict = pub_sub_comment_instance.to_dict()
# create an instance of PubSubComment from a dict
pub_sub_comment_from_dict = PubSubComment.from_dict(pub_sub_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


