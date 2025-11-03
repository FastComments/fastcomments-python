# FComment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**url_id** | **str** |  | 
**url_id_raw** | **str** |  | [optional] 
**url** | **str** |  | 
**page_title** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**anon_user_id** | **str** |  | [optional] 
**commenter_email** | **str** |  | [optional] 
**commenter_name** | **str** |  | 
**commenter_link** | **str** |  | [optional] 
**comment** | **str** |  | 
**comment_html** | **str** |  | 
**parent_id** | **str** |  | [optional] 
**var_date** | **datetime** |  | 
**local_date_string** | **str** |  | [optional] 
**local_date_hours** | **int** |  | [optional] 
**votes** | **int** |  | [optional] 
**votes_up** | **int** |  | [optional] 
**votes_down** | **int** |  | [optional] 
**expire_at** | **datetime** |  | [optional] 
**verified** | **bool** |  | 
**verified_date** | **datetime** |  | [optional] 
**verification_id** | **str** |  | [optional] 
**notification_sent_for_parent** | **bool** |  | [optional] 
**notification_sent_for_parent_tenant** | **bool** |  | [optional] 
**reviewed** | **bool** |  | [optional] 
**imported** | **bool** |  | [optional] 
**external_id** | **str** |  | [optional] 
**external_parent_id** | **str** |  | [optional] 
**avatar_src** | **str** |  | [optional] 
**is_spam** | **bool** |  | [optional] 
**perm_not_spam** | **bool** |  | [optional] 
**ai_determined_spam** | **bool** |  | [optional] 
**has_images** | **bool** |  | [optional] 
**page_number** | **int** |  | [optional] 
**page_number_of** | **int** |  | [optional] 
**page_number_nf** | **int** |  | [optional] 
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
**from_product_id** | **int** |  | [optional] 
**meta** | [**FCommentMeta**](FCommentMeta.md) |  | [optional] 
**ip_hash** | **str** |  | [optional] 
**mentions** | [**List[CommentUserMentionInfo]**](CommentUserMentionInfo.md) |  | [optional] 
**hash_tags** | [**List[CommentUserHashTagInfo]**](CommentUserHashTagInfo.md) |  | [optional] 
**badges** | [**List[CommentUserBadgeInfo]**](CommentUserBadgeInfo.md) |  | [optional] 
**domain** | **str** |  | [optional] 
**veteran_badge_processed** | **str** |  | [optional] 
**moderation_group_ids** | **List[str]** |  | [optional] 
**did_process_badges** | **bool** |  | [optional] 
**from_offline_restore** | **bool** |  | [optional] 
**autoplay_job_id** | **str** |  | [optional] 
**autoplay_delay_ms** | **int** |  | [optional] 
**feedback_ids** | **List[str]** |  | [optional] 
**logs** | **List[List[object]]** |  | [optional] 
**group_ids** | **List[str]** |  | [optional] 
**view_count** | **int** |  | [optional] 
**requires_verification** | **bool** |  | [optional] 
**edit_key** | **str** |  | [optional] 

## Example

```python
from generated.models.f_comment import FComment

# TODO update the JSON string below
json = "{}"
# create an instance of FComment from a JSON string
f_comment_instance = FComment.from_json(json)
# print the JSON string representation of the object
print(FComment.to_json())

# convert the object into a dict
f_comment_dict = f_comment_instance.to_dict()
# create an instance of FComment from a dict
f_comment_from_dict = FComment.from_dict(f_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


