# UpdatableCommentParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url_id** | **str** |  | [optional] 
**url_id_raw** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**page_title** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**commenter_email** | **str** |  | [optional] 
**commenter_name** | **str** |  | [optional] 
**commenter_link** | **str** |  | [optional] 
**comment** | **str** |  | [optional] 
**comment_html** | **str** |  | [optional] 
**parent_id** | **str** |  | [optional] 
**var_date** | **float** |  | [optional] 
**local_date_string** | **str** |  | [optional] 
**local_date_hours** | **int** |  | [optional] 
**votes** | **int** |  | [optional] 
**votes_up** | **int** |  | [optional] 
**votes_down** | **int** |  | [optional] 
**expire_at** | **datetime** |  | [optional] 
**verified** | **bool** |  | [optional] 
**verified_date** | **datetime** |  | [optional] 
**notification_sent_for_parent** | **bool** |  | [optional] 
**notification_sent_for_parent_tenant** | **bool** |  | [optional] 
**reviewed** | **bool** |  | [optional] 
**external_id** | **str** |  | [optional] 
**external_parent_id** | **str** |  | [optional] 
**avatar_src** | **str** |  | [optional] 
**is_spam** | **bool** |  | [optional] 
**approved** | **bool** |  | [optional] 
**is_deleted** | **bool** |  | [optional] 
**is_deleted_user** | **bool** |  | [optional] 
**is_by_admin** | **bool** |  | [optional] 
**is_by_moderator** | **bool** |  | [optional] 
**is_pinned** | **bool** |  | [optional] 
**is_locked** | **bool** |  | [optional] 
**flag_count** | **int** |  | [optional] 
**display_label** | **str** |  | [optional] 
**meta** | [**FCommentMeta**](FCommentMeta.md) |  | [optional] 
**moderation_group_ids** | **List[str]** |  | [optional] 
**feedback_ids** | **List[str]** |  | [optional] 

## Example

```python
from client.models.updatable_comment_params import UpdatableCommentParams

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatableCommentParams from a JSON string
updatable_comment_params_instance = UpdatableCommentParams.from_json(json)
# print the JSON string representation of the object
print(UpdatableCommentParams.to_json())

# convert the object into a dict
updatable_comment_params_dict = updatable_comment_params_instance.to_dict()
# create an instance of UpdatableCommentParams from a dict
updatable_comment_params_from_dict = UpdatableCommentParams.from_dict(updatable_comment_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


