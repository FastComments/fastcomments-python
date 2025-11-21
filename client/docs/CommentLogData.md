# CommentLogData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clear_content** | **bool** |  | [optional] 
**is_deleted_user** | **bool** |  | [optional] 
**phrase** | **str** |  | [optional] 
**bad_word** | **str** |  | [optional] 
**word** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**tenant_badge_id** | **str** |  | [optional] 
**badge_id** | **str** |  | [optional] 
**was_logged_in** | **bool** |  | [optional] 
**found_user** | **bool** |  | [optional] 
**verified** | **bool** |  | [optional] 
**engine** | **str** |  | [optional] 
**engine_response** | **str** |  | [optional] 
**engine_tokens** | **float** |  | [optional] 
**trust_factor** | **float** |  | [optional] 
**rule** | [**SpamRule**](SpamRule.md) |  | [optional] 
**user_id** | **str** |  | [optional] 
**subscribers** | **float** |  | [optional] 
**notification_count** | **float** |  | [optional] 
**votes_before** | **float** |  | [optional] 
**votes_up_before** | **float** |  | [optional] 
**votes_down_before** | **float** |  | [optional] 
**votes_after** | **float** |  | [optional] 
**votes_up_after** | **float** |  | [optional] 
**votes_down_after** | **float** |  | [optional] 
**repeat_action** | [**RepeatCommentHandlingAction**](RepeatCommentHandlingAction.md) |  | [optional] 
**reason** | [**RepeatCommentCheckIgnoredReason**](RepeatCommentCheckIgnoredReason.md) |  | [optional] 
**other_data** | **object** |  | [optional] 
**spam_before** | **bool** |  | [optional] 
**spam_after** | **bool** |  | [optional] 
**permanent_flag** | **str** |  | [optional] 
**approved_before** | **bool** |  | [optional] 
**approved_after** | **bool** |  | [optional] 
**reviewed_before** | **bool** |  | [optional] 
**reviewed_after** | **bool** |  | [optional] 
**text_before** | **str** |  | [optional] 
**text_after** | **str** |  | [optional] 
**expire_before** | **datetime** |  | [optional] 
**expire_after** | **datetime** |  | [optional] 
**flag_count_before** | **float** |  | [optional] 
**trust_factor_before** | **float** |  | [optional] 
**trust_factor_after** | **float** |  | [optional] 
**referenced_comment_id** | **str** |  | [optional] 

## Example

```python
from client.models.comment_log_data import CommentLogData

# TODO update the JSON string below
json = "{}"
# create an instance of CommentLogData from a JSON string
comment_log_data_instance = CommentLogData.from_json(json)
# print the JSON string representation of the object
print(CommentLogData.to_json())

# convert the object into a dict
comment_log_data_dict = comment_log_data_instance.to_dict()
# create an instance of CommentLogData from a dict
comment_log_data_from_dict = CommentLogData.from_dict(comment_log_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


