# GetBanUsersFromCommentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**banned_users** | [**List[APIBannedUserWithMultiMatchInfo]**](APIBannedUserWithMultiMatchInfo.md) |  | 
**code** | **str** |  | 
**status** | [**APIStatus**](APIStatus.md) |  | 
**reason** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.get_ban_users_from_comment_response import GetBanUsersFromCommentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetBanUsersFromCommentResponse from a JSON string
get_ban_users_from_comment_response_instance = GetBanUsersFromCommentResponse.from_json(json)
# print the JSON string representation of the object
print(GetBanUsersFromCommentResponse.to_json())

# convert the object into a dict
get_ban_users_from_comment_response_dict = get_ban_users_from_comment_response_instance.to_dict()
# create an instance of GetBanUsersFromCommentResponse from a dict
get_ban_users_from_comment_response_from_dict = GetBanUsersFromCommentResponse.from_dict(get_ban_users_from_comment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


