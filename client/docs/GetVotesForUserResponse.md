# GetVotesForUserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**applied_authorized_votes** | [**List[PublicVote]**](PublicVote.md) |  | 
**applied_anonymous_votes** | [**List[PublicVote]**](PublicVote.md) |  | 
**pending_votes** | [**List[PublicVote]**](PublicVote.md) |  | 

## Example

```python
from client.models.get_votes_for_user_response import GetVotesForUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetVotesForUserResponse from a JSON string
get_votes_for_user_response_instance = GetVotesForUserResponse.from_json(json)
# print the JSON string representation of the object
print(GetVotesForUserResponse.to_json())

# convert the object into a dict
get_votes_for_user_response_dict = get_votes_for_user_response_instance.to_dict()
# create an instance of GetVotesForUserResponse from a dict
get_votes_for_user_response_from_dict = GetVotesForUserResponse.from_dict(get_votes_for_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


