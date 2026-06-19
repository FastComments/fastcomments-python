# ModerationFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reviewed** | **bool** |  | [optional] 
**approved** | **bool** |  | [optional] 
**is_spam** | **bool** |  | [optional] 
**is_banned_user** | **bool** |  | [optional] 
**is_locked** | **bool** |  | [optional] 
**flag_count_gt** | **float** |  | [optional] 
**user_id** | **str** |  | [optional] 
**url_id** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 
**moderation_group_ids** | **List[str]** |  | [optional] 
**comment_text_search** | **List[str]** | Text search terms. Each term is matched case-insensitively against the comment text. A term wrapped in quotes means exact phrase match. | [optional] 
**exact_comment_text** | **str** | Set by the &#x60;exact&#x3D;\&quot;...\&quot;&#x60; search syntax. The comment text must equal this value exactly (case-sensitive, full-string), as opposed to the substring matching of commentTextSearch. | [optional] 

## Example

```python
from client.models.moderation_filter import ModerationFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ModerationFilter from a JSON string
moderation_filter_instance = ModerationFilter.from_json(json)
# print the JSON string representation of the object
print(ModerationFilter.to_json())

# convert the object into a dict
moderation_filter_dict = moderation_filter_instance.to_dict()
# create an instance of ModerationFilter from a dict
moderation_filter_from_dict = ModerationFilter.from_dict(moderation_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


