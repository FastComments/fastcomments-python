# CommentData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **int** |  | [optional] 
**local_date_string** | **str** |  | [optional] 
**local_date_hours** | **int** |  | [optional] 
**commenter_name** | **str** |  | 
**commenter_email** | **str** |  | [optional] 
**commenter_link** | **str** |  | [optional] 
**comment** | **str** |  | 
**product_id** | **int** |  | [optional] 
**user_id** | **str** |  | [optional] 
**avatar_src** | **str** |  | [optional] 
**parent_id** | **str** |  | [optional] 
**mentions** | [**List[CommentUserMentionInfo]**](CommentUserMentionInfo.md) |  | [optional] 
**hash_tags** | [**List[CommentUserHashTagInfo]**](CommentUserHashTagInfo.md) |  | [optional] 
**page_title** | **str** |  | [optional] 
**is_from_my_account_page** | **bool** |  | [optional] 
**url** | **str** |  | 
**url_id** | **str** |  | 
**meta** | **object** |  | [optional] 
**moderation_group_ids** | **List[str]** |  | [optional] 
**rating** | **float** |  | [optional] 
**from_offline_restore** | **bool** |  | [optional] 
**autoplay_delay_ms** | **int** |  | [optional] 
**feedback_ids** | **List[str]** |  | [optional] 
**question_values** | [**Dict[str, RecordStringStringOrNumberValue]**](RecordStringStringOrNumberValue.md) | Construct a type with a set of properties K of type T | [optional] 

## Example

```python
from generated.models.comment_data import CommentData

# TODO update the JSON string below
json = "{}"
# create an instance of CommentData from a JSON string
comment_data_instance = CommentData.from_json(json)
# print the JSON string representation of the object
print(CommentData.to_json())

# convert the object into a dict
comment_data_dict = comment_data_instance.to_dict()
# create an instance of CommentData from a dict
comment_data_from_dict = CommentData.from_dict(comment_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


