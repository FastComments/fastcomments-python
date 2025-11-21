# CommentLogEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**d** | **datetime** |  | 
**t** | [**CommentLogType**](CommentLogType.md) |  | 
**da** | [**CommentLogData**](CommentLogData.md) |  | [optional] 

## Example

```python
from client.models.comment_log_entry import CommentLogEntry

# TODO update the JSON string below
json = "{}"
# create an instance of CommentLogEntry from a JSON string
comment_log_entry_instance = CommentLogEntry.from_json(json)
# print the JSON string representation of the object
print(CommentLogEntry.to_json())

# convert the object into a dict
comment_log_entry_dict = comment_log_entry_instance.to_dict()
# create an instance of CommentLogEntry from a dict
comment_log_entry_from_dict = CommentLogEntry.from_dict(comment_log_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


