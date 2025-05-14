# CreateCommentParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **float** |  | 
**local_date_string** | **str** |  | [optional] 
**local_date_hours** | **float** |  | [optional] 
**commenter_name** | **str** |  | 
**commenter_email** | **str** |  | [optional] 
**commenter_link** | **str** |  | [optional] 
**comment** | **str** |  | 
**product_id** | **float** |  | [optional] 
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
**autoplay_delay_ms** | **float** |  | [optional] 
**feedback_ids** | **List[str]** |  | [optional] 
**question_values** | [**Dict[str, RecordStringStringOrNumberValue]**](RecordStringStringOrNumberValue.md) | Construct a type with a set of properties K of type T | [optional] 
**approved** | **bool** |  | [optional] 
**domain** | **str** |  | [optional] 
**ip** | **str** |  | [optional] 
**is_pinned** | **bool** |  | [optional] 
**locale** | **str** | Example: en_us | 
**reviewed** | **bool** |  | [optional] 
**verified** | **bool** |  | [optional] 
**votes** | **float** |  | [optional] 
**votes_down** | **float** |  | [optional] 
**votes_up** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.create_comment_params import CreateCommentParams

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCommentParams from a JSON string
create_comment_params_instance = CreateCommentParams.from_json(json)
# print the JSON string representation of the object
print(CreateCommentParams.to_json())

# convert the object into a dict
create_comment_params_dict = create_comment_params_instance.to_dict()
# create an instance of CreateCommentParams from a dict
create_comment_params_from_dict = CreateCommentParams.from_dict(create_comment_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


