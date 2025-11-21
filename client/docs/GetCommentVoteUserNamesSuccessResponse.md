# GetCommentVoteUserNamesSuccessResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**vote_user_names** | **List[str]** |  | 
**has_more** | **bool** |  | 

## Example

```python
from client.models.get_comment_vote_user_names_success_response import GetCommentVoteUserNamesSuccessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCommentVoteUserNamesSuccessResponse from a JSON string
get_comment_vote_user_names_success_response_instance = GetCommentVoteUserNamesSuccessResponse.from_json(json)
# print the JSON string representation of the object
print(GetCommentVoteUserNamesSuccessResponse.to_json())

# convert the object into a dict
get_comment_vote_user_names_success_response_dict = get_comment_vote_user_names_success_response_instance.to_dict()
# create an instance of GetCommentVoteUserNamesSuccessResponse from a dict
get_comment_vote_user_names_success_response_from_dict = GetCommentVoteUserNamesSuccessResponse.from_dict(get_comment_vote_user_names_success_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


