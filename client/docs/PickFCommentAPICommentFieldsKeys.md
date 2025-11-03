# PickFCommentAPICommentFieldsKeys

From T, pick a set of properties whose keys are in the union K

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** |  | 
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
**local_date_string** | **str** |  | [optional] 
**local_date_hours** | **int** |  | [optional] 
**votes** | **int** |  | [optional] 
**votes_up** | **int** |  | [optional] 
**votes_down** | **int** |  | [optional] 
**expire_at** | **datetime** |  | [optional] 
**verified** | **bool** |  | 
**verified_date** | **datetime** |  | [optional] 
**notification_sent_for_parent** | **bool** |  | [optional] 
**notification_sent_for_parent_tenant** | **bool** |  | [optional] 
**reviewed** | **bool** |  | [optional] 
**external_id** | **str** |  | [optional] 
**external_parent_id** | **str** |  | [optional] 
**avatar_src** | **str** |  | [optional] 
**is_spam** | **bool** |  | [optional] 
**ai_determined_spam** | **bool** |  | [optional] 
**has_images** | **bool** |  | [optional] 
**has_links** | **bool** |  | [optional] 
**has_code** | **bool** |  | [optional] 
**approved** | **bool** |  | 
**locale** | **str** |  | 
**is_deleted** | **bool** |  | [optional] 
**is_deleted_user** | **bool** |  | [optional] 
**is_by_admin** | **bool** |  | [optional] 
**is_by_moderator** | **bool** |  | [optional] 
**is_pinned** | **bool** |  | [optional] 
**is_locked** | **bool** |  | [optional] 
**flag_count** | **int** |  | [optional] 
**rating** | **float** |  | [optional] 
**display_label** | **str** |  | [optional] 
**from_product_id** | **int** |  | [optional] 
**meta** | [**PickFCommentAPICommentFieldsKeysMeta**](PickFCommentAPICommentFieldsKeysMeta.md) |  | [optional] 
**mentions** | [**List[CommentUserMentionInfo]**](CommentUserMentionInfo.md) |  | [optional] 
**hash_tags** | [**List[CommentUserHashTagInfo]**](CommentUserHashTagInfo.md) |  | [optional] 
**badges** | [**List[CommentUserBadgeInfo]**](CommentUserBadgeInfo.md) |  | [optional] 
**domain** | **str** |  | [optional] 
**moderation_group_ids** | **List[str]** |  | [optional] 
**feedback_ids** | **List[str]** |  | [optional] 

## Example

```python
from client.models.pick_f_comment_api_comment_fields_keys import PickFCommentAPICommentFieldsKeys

# TODO update the JSON string below
json = "{}"
# create an instance of PickFCommentAPICommentFieldsKeys from a JSON string
pick_f_comment_api_comment_fields_keys_instance = PickFCommentAPICommentFieldsKeys.from_json(json)
# print the JSON string representation of the object
print(PickFCommentAPICommentFieldsKeys.to_json())

# convert the object into a dict
pick_f_comment_api_comment_fields_keys_dict = pick_f_comment_api_comment_fields_keys_instance.to_dict()
# create an instance of PickFCommentAPICommentFieldsKeys from a dict
pick_f_comment_api_comment_fields_keys_from_dict = PickFCommentAPICommentFieldsKeys.from_dict(pick_f_comment_api_comment_fields_keys_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


