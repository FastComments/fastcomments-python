# PickFCommentPublicCommentFieldsKeys

From T, pick a set of properties whose keys are in the union K

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** |  | 
**id** | **str** |  | 
**user_id** | **str** |  | [optional] 
**anon_user_id** | **str** |  | [optional] 
**commenter_name** | **str** |  | 
**commenter_link** | **str** |  | [optional] 
**comment_html** | **str** |  | 
**parent_id** | **str** |  | [optional] 
**votes** | **int** |  | [optional] 
**votes_up** | **int** |  | [optional] 
**votes_down** | **int** |  | [optional] 
**verified** | **bool** |  | 
**avatar_src** | **str** |  | [optional] 
**is_spam** | **bool** |  | [optional] 
**has_images** | **bool** |  | [optional] 
**is_deleted** | **bool** |  | [optional] 
**is_deleted_user** | **bool** |  | [optional] 
**is_by_admin** | **bool** |  | [optional] 
**is_by_moderator** | **bool** |  | [optional] 
**is_pinned** | **bool** |  | [optional] 
**is_locked** | **bool** |  | [optional] 
**rating** | **float** |  | [optional] 
**display_label** | **str** |  | [optional] 
**badges** | [**List[CommentUserBadgeInfo]**](CommentUserBadgeInfo.md) |  | [optional] 
**feedback_ids** | **List[str]** |  | [optional] 
**view_count** | **int** |  | [optional] 
**requires_verification** | **bool** |  | [optional] 
**edit_key** | **str** |  | [optional] 

## Example

```python
from client.models.pick_f_comment_public_comment_fields_keys import PickFCommentPublicCommentFieldsKeys

# TODO update the JSON string below
json = "{}"
# create an instance of PickFCommentPublicCommentFieldsKeys from a JSON string
pick_f_comment_public_comment_fields_keys_instance = PickFCommentPublicCommentFieldsKeys.from_json(json)
# print the JSON string representation of the object
print(PickFCommentPublicCommentFieldsKeys.to_json())

# convert the object into a dict
pick_f_comment_public_comment_fields_keys_dict = pick_f_comment_public_comment_fields_keys_instance.to_dict()
# create an instance of PickFCommentPublicCommentFieldsKeys from a dict
pick_f_comment_public_comment_fields_keys_from_dict = PickFCommentPublicCommentFieldsKeys.from_dict(pick_f_comment_public_comment_fields_keys_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


