# BanUserFromCommentResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**changelog** | [**APIBanUserChangeLog**](APIBanUserChangeLog.md) |  | [optional] 
**code** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 

## Example

```python
from client.models.ban_user_from_comment_result import BanUserFromCommentResult

# TODO update the JSON string below
json = "{}"
# create an instance of BanUserFromCommentResult from a JSON string
ban_user_from_comment_result_instance = BanUserFromCommentResult.from_json(json)
# print the JSON string representation of the object
print(BanUserFromCommentResult.to_json())

# convert the object into a dict
ban_user_from_comment_result_dict = ban_user_from_comment_result_instance.to_dict()
# create an instance of BanUserFromCommentResult from a dict
ban_user_from_comment_result_from_dict = BanUserFromCommentResult.from_dict(ban_user_from_comment_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


