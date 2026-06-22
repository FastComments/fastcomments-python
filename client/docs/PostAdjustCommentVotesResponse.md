# PostAdjustCommentVotesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**new_comment_votes** | **int** |  | 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.post_adjust_comment_votes_response import PostAdjustCommentVotesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostAdjustCommentVotesResponse from a JSON string
post_adjust_comment_votes_response_instance = PostAdjustCommentVotesResponse.from_json(json)
# print the JSON string representation of the object
print(PostAdjustCommentVotesResponse.to_json())

# convert the object into a dict
post_adjust_comment_votes_response_dict = post_adjust_comment_votes_response_instance.to_dict()
# create an instance of PostAdjustCommentVotesResponse from a dict
post_adjust_comment_votes_response_from_dict = PostAdjustCommentVotesResponse.from_dict(post_adjust_comment_votes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


