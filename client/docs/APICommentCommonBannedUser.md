# APICommentCommonBannedUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user_id** | **str** |  | [optional] 
**ban_type** | **str** |  | 
**email** | **str** |  | [optional] 
**ip_hash** | **str** |  | [optional] 
**banned_until** | **datetime** |  | 
**has_email_wildcard** | **bool** |  | 
**ban_reason** | **str** |  | [optional] 

## Example

```python
from client.models.api_comment_common_banned_user import APICommentCommonBannedUser

# TODO update the JSON string below
json = "{}"
# create an instance of APICommentCommonBannedUser from a JSON string
api_comment_common_banned_user_instance = APICommentCommonBannedUser.from_json(json)
# print the JSON string representation of the object
print(APICommentCommonBannedUser.to_json())

# convert the object into a dict
api_comment_common_banned_user_dict = api_comment_common_banned_user_instance.to_dict()
# create an instance of APICommentCommonBannedUser from a dict
api_comment_common_banned_user_from_dict = APICommentCommonBannedUser.from_dict(api_comment_common_banned_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


