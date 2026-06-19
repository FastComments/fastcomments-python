# ModerationAPICommentLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** |  | 
**username** | **str** |  | [optional] 
**action_name** | **str** |  | 
**message_html** | **str** |  | 

## Example

```python
from client.models.moderation_api_comment_log import ModerationAPICommentLog

# TODO update the JSON string below
json = "{}"
# create an instance of ModerationAPICommentLog from a JSON string
moderation_api_comment_log_instance = ModerationAPICommentLog.from_json(json)
# print the JSON string representation of the object
print(ModerationAPICommentLog.to_json())

# convert the object into a dict
moderation_api_comment_log_dict = moderation_api_comment_log_instance.to_dict()
# create an instance of ModerationAPICommentLog from a dict
moderation_api_comment_log_from_dict = ModerationAPICommentLog.from_dict(moderation_api_comment_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


