# VoteCommentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**vote_id** | **str** |  | [optional] 
**is_verified** | **bool** |  | [optional] 
**user** | [**VoteResponseUser**](VoteResponseUser.md) |  | [optional] 
**edit_key** | **str** |  | [optional] 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.vote_comment_response import VoteCommentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VoteCommentResponse from a JSON string
vote_comment_response_instance = VoteCommentResponse.from_json(json)
# print the JSON string representation of the object
print(VoteCommentResponse.to_json())

# convert the object into a dict
vote_comment_response_dict = vote_comment_response_instance.to_dict()
# create an instance of VoteCommentResponse from a dict
vote_comment_response_from_dict = VoteCommentResponse.from_dict(vote_comment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


