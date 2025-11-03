# PickAPICommentUpdatableCommentFields

From T, pick a set of properties whose keys are in the union K

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** |  | 
**url_id** | **str** |  | 
**url_id_raw** | **str** |  | [optional] 
**url** | **str** |  | 
**page_title** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
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
**approved** | **bool** |  | 
**is_deleted** | **bool** |  | [optional] 
**is_deleted_user** | **bool** |  | [optional] 
**is_by_admin** | **bool** |  | [optional] 
**is_by_moderator** | **bool** |  | [optional] 
**is_pinned** | **bool** |  | [optional] 
**is_locked** | **bool** |  | [optional] 
**flag_count** | **int** |  | [optional] 
**display_label** | **str** |  | [optional] 
**meta** | [**PickFCommentAPICommentFieldsKeysMeta**](PickFCommentAPICommentFieldsKeysMeta.md) |  | [optional] 
**moderation_group_ids** | **List[str]** |  | [optional] 
**feedback_ids** | **List[str]** |  | [optional] 

## Example

```python
from generated.models.pick_api_comment_updatable_comment_fields import PickAPICommentUpdatableCommentFields

# TODO update the JSON string below
json = "{}"
# create an instance of PickAPICommentUpdatableCommentFields from a JSON string
pick_api_comment_updatable_comment_fields_instance = PickAPICommentUpdatableCommentFields.from_json(json)
# print the JSON string representation of the object
print(PickAPICommentUpdatableCommentFields.to_json())

# convert the object into a dict
pick_api_comment_updatable_comment_fields_dict = pick_api_comment_updatable_comment_fields_instance.to_dict()
# create an instance of PickAPICommentUpdatableCommentFields from a dict
pick_api_comment_updatable_comment_fields_from_dict = PickAPICommentUpdatableCommentFields.from_dict(pick_api_comment_updatable_comment_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


