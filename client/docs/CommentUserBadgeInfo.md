# CommentUserBadgeInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **int** |  | 
**description** | **str** |  | 
**display_label** | **str** |  | [optional] 
**display_src** | **str** |  | [optional] 
**background_color** | **str** |  | [optional] 
**border_color** | **str** |  | [optional] 
**text_color** | **str** |  | [optional] 
**css_class** | **str** |  | [optional] 

## Example

```python
from client.models.comment_user_badge_info import CommentUserBadgeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CommentUserBadgeInfo from a JSON string
comment_user_badge_info_instance = CommentUserBadgeInfo.from_json(json)
# print the JSON string representation of the object
print(CommentUserBadgeInfo.to_json())

# convert the object into a dict
comment_user_badge_info_dict = comment_user_badge_info_instance.to_dict()
# create an instance of CommentUserBadgeInfo from a dict
comment_user_badge_info_from_dict = CommentUserBadgeInfo.from_dict(comment_user_badge_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


