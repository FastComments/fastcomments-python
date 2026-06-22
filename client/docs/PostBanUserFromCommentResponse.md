# PostBanUserFromCommentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**changelog** | [**APIBanUserChangeLog**](APIBanUserChangeLog.md) |  | [optional] 
**code** | **str** |  | 
**reason** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.post_ban_user_from_comment_response import PostBanUserFromCommentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostBanUserFromCommentResponse from a JSON string
post_ban_user_from_comment_response_instance = PostBanUserFromCommentResponse.from_json(json)
# print the JSON string representation of the object
print(PostBanUserFromCommentResponse.to_json())

# convert the object into a dict
post_ban_user_from_comment_response_dict = post_ban_user_from_comment_response_instance.to_dict()
# create an instance of PostBanUserFromCommentResponse from a dict
post_ban_user_from_comment_response_from_dict = PostBanUserFromCommentResponse.from_dict(post_ban_user_from_comment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


