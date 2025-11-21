# APIComment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**ai_determined_spam** | **bool** |  | [optional] 
**anon_user_id** | **str** |  | [optional] 
**approved** | **bool** |  | 
**avatar_src** | **str** |  | [optional] 
**badges** | [**List[CommentUserBadgeInfo]**](CommentUserBadgeInfo.md) |  | [optional] 
**comment** | **str** |  | 
**comment_html** | **str** |  | 
**commenter_email** | **str** |  | [optional] 
**commenter_link** | **str** |  | [optional] 
**commenter_name** | **str** |  | 
**var_date** | **float** |  | 
**display_label** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 
**external_id** | **str** |  | [optional] 
**external_parent_id** | **str** |  | [optional] 
**expire_at** | **datetime** |  | [optional] 
**feedback_ids** | **List[str]** |  | [optional] 
**flag_count** | **int** |  | [optional] 
**from_product_id** | **int** |  | [optional] 
**has_code** | **bool** |  | [optional] 
**has_images** | **bool** |  | [optional] 
**has_links** | **bool** |  | [optional] 
**hash_tags** | [**List[CommentUserHashTagInfo]**](CommentUserHashTagInfo.md) |  | [optional] 
**is_by_admin** | **bool** |  | [optional] 
**is_by_moderator** | **bool** |  | [optional] 
**is_deleted** | **bool** |  | [optional] 
**is_deleted_user** | **bool** |  | [optional] 
**is_pinned** | **bool** |  | [optional] 
**is_locked** | **bool** |  | [optional] 
**is_spam** | **bool** |  | [optional] 
**local_date_hours** | **int** |  | [optional] 
**local_date_string** | **str** |  | [optional] 
**locale** | **str** |  | 
**mentions** | [**List[CommentUserMentionInfo]**](CommentUserMentionInfo.md) |  | [optional] 
**meta** | [**FCommentMeta**](FCommentMeta.md) |  | [optional] 
**moderation_group_ids** | **List[str]** |  | [optional] 
**notification_sent_for_parent** | **bool** |  | [optional] 
**notification_sent_for_parent_tenant** | **bool** |  | [optional] 
**page_title** | **str** |  | [optional] 
**parent_id** | **str** |  | [optional] 
**rating** | **float** |  | [optional] 
**reviewed** | **bool** |  | [optional] 
**tenant_id** | **str** |  | 
**url** | **str** |  | 
**url_id** | **str** |  | 
**url_id_raw** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**verified** | **bool** |  | 
**verified_date** | **datetime** |  | [optional] 
**votes** | **int** |  | [optional] 
**votes_down** | **int** |  | [optional] 
**votes_up** | **int** |  | [optional] 

## Example

```python
from client.models.api_comment import APIComment

# TODO update the JSON string below
json = "{}"
# create an instance of APIComment from a JSON string
api_comment_instance = APIComment.from_json(json)
# print the JSON string representation of the object
print(APIComment.to_json())

# convert the object into a dict
api_comment_dict = api_comment_instance.to_dict()
# create an instance of APIComment from a dict
api_comment_from_dict = APIComment.from_dict(api_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


