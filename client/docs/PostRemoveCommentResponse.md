# PostRemoveCommentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
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
from client.models.post_remove_comment_response import PostRemoveCommentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostRemoveCommentResponse from a JSON string
post_remove_comment_response_instance = PostRemoveCommentResponse.from_json(json)
# print the JSON string representation of the object
print(PostRemoveCommentResponse.to_json())

# convert the object into a dict
post_remove_comment_response_dict = post_remove_comment_response_instance.to_dict()
# create an instance of PostRemoveCommentResponse from a dict
post_remove_comment_response_from_dict = PostRemoveCommentResponse.from_dict(post_remove_comment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


