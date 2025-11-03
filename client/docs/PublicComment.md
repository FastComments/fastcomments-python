# PublicComment


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
**is_unread** | **bool** |  | [optional] 
**my_vote_id** | **str** |  | [optional] 
**is_voted_down** | **bool** |  | [optional] 
**is_voted_up** | **bool** |  | [optional] 
**has_children** | **bool** | This is always set when asTree&#x3D;true | [optional] 
**nested_children_count** | **int** | The total nested child count included in this response (may be more available w/ pagination) Only set with asTree&#x3D;true, otherwise this will be null. | [optional] 
**child_count** | **int** | You must ask the API to count children (with asTree&#x3D;true&amp;countChildren&#x3D;true), otherwise this will be null. This will be the complete direct child count, whereas children may only contain a subset based on pagination. | [optional] 
**children** | [**List[PublicComment]**](PublicComment.md) |  | [optional] 
**is_flagged** | **bool** |  | [optional] 
**is_blocked** | **bool** |  | [optional] 

## Example

```python
from generated.models.public_comment import PublicComment

# TODO update the JSON string below
json = "{}"
# create an instance of PublicComment from a JSON string
public_comment_instance = PublicComment.from_json(json)
# print the JSON string representation of the object
print(PublicComment.to_json())

# convert the object into a dict
public_comment_dict = public_comment_instance.to_dict()
# create an instance of PublicComment from a dict
public_comment_from_dict = PublicComment.from_dict(public_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


