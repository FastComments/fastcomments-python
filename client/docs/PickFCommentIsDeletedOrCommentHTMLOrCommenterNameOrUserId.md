# PickFCommentIsDeletedOrCommentHTMLOrCommenterNameOrUserId

From T, pick a set of properties whose keys are in the union K

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | [optional] 
**commenter_name** | **str** |  | 
**comment_html** | **str** |  | 
**is_deleted** | **bool** |  | [optional] 

## Example

```python
from client.models.pick_f_comment_is_deleted_or_comment_htmlor_commenter_name_or_user_id import PickFCommentIsDeletedOrCommentHTMLOrCommenterNameOrUserId

# TODO update the JSON string below
json = "{}"
# create an instance of PickFCommentIsDeletedOrCommentHTMLOrCommenterNameOrUserId from a JSON string
pick_f_comment_is_deleted_or_comment_htmlor_commenter_name_or_user_id_instance = PickFCommentIsDeletedOrCommentHTMLOrCommenterNameOrUserId.from_json(json)
# print the JSON string representation of the object
print(PickFCommentIsDeletedOrCommentHTMLOrCommenterNameOrUserId.to_json())

# convert the object into a dict
pick_f_comment_is_deleted_or_comment_htmlor_commenter_name_or_user_id_dict = pick_f_comment_is_deleted_or_comment_htmlor_commenter_name_or_user_id_instance.to_dict()
# create an instance of PickFCommentIsDeletedOrCommentHTMLOrCommenterNameOrUserId from a dict
pick_f_comment_is_deleted_or_comment_htmlor_commenter_name_or_user_id_from_dict = PickFCommentIsDeletedOrCommentHTMLOrCommenterNameOrUserId.from_dict(pick_f_comment_is_deleted_or_comment_htmlor_commenter_name_or_user_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


