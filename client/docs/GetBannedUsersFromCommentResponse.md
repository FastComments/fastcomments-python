# GetBannedUsersFromCommentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**banned_users** | [**List[APIBannedUserWithMultiMatchInfo]**](APIBannedUserWithMultiMatchInfo.md) |  | 
**code** | **str** |  | [optional] 
**status** | [**APIStatus**](APIStatus.md) |  | 

## Example

```python
from client.models.get_banned_users_from_comment_response import GetBannedUsersFromCommentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetBannedUsersFromCommentResponse from a JSON string
get_banned_users_from_comment_response_instance = GetBannedUsersFromCommentResponse.from_json(json)
# print the JSON string representation of the object
print(GetBannedUsersFromCommentResponse.to_json())

# convert the object into a dict
get_banned_users_from_comment_response_dict = get_banned_users_from_comment_response_instance.to_dict()
# create an instance of GetBannedUsersFromCommentResponse from a dict
get_banned_users_from_comment_response_from_dict = GetBannedUsersFromCommentResponse.from_dict(get_banned_users_from_comment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


