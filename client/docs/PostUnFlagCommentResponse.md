# PostUnFlagCommentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.post_un_flag_comment_response import PostUnFlagCommentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostUnFlagCommentResponse from a JSON string
post_un_flag_comment_response_instance = PostUnFlagCommentResponse.from_json(json)
# print the JSON string representation of the object
print(PostUnFlagCommentResponse.to_json())

# convert the object into a dict
post_un_flag_comment_response_dict = post_un_flag_comment_response_instance.to_dict()
# create an instance of PostUnFlagCommentResponse from a dict
post_un_flag_comment_response_from_dict = PostUnFlagCommentResponse.from_dict(post_un_flag_comment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


