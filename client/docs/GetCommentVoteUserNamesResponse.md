# GetCommentVoteUserNamesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**vote_user_names** | **List[str]** |  | 
**has_more** | **bool** |  | 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.get_comment_vote_user_names_response import GetCommentVoteUserNamesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCommentVoteUserNamesResponse from a JSON string
get_comment_vote_user_names_response_instance = GetCommentVoteUserNamesResponse.from_json(json)
# print the JSON string representation of the object
print(GetCommentVoteUserNamesResponse.to_json())

# convert the object into a dict
get_comment_vote_user_names_response_dict = get_comment_vote_user_names_response_instance.to_dict()
# create an instance of GetCommentVoteUserNamesResponse from a dict
get_comment_vote_user_names_response_from_dict = GetCommentVoteUserNamesResponse.from_dict(get_comment_vote_user_names_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


