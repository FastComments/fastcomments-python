# PostVoteResponse


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
from client.models.post_vote_response import PostVoteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostVoteResponse from a JSON string
post_vote_response_instance = PostVoteResponse.from_json(json)
# print the JSON string representation of the object
print(PostVoteResponse.to_json())

# convert the object into a dict
post_vote_response_dict = post_vote_response_instance.to_dict()
# create an instance of PostVoteResponse from a dict
post_vote_response_from_dict = PostVoteResponse.from_dict(post_vote_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


