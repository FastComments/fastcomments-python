# GetVotesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**applied_authorized_votes** | [**List[PublicVote]**](PublicVote.md) |  | 
**applied_anonymous_votes** | [**List[PublicVote]**](PublicVote.md) |  | 
**pending_votes** | [**List[PublicVote]**](PublicVote.md) |  | 

## Example

```python
from client.models.get_votes_response import GetVotesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetVotesResponse from a JSON string
get_votes_response_instance = GetVotesResponse.from_json(json)
# print the JSON string representation of the object
print(GetVotesResponse.to_json())

# convert the object into a dict
get_votes_response_dict = get_votes_response_instance.to_dict()
# create an instance of GetVotesResponse from a dict
get_votes_response_from_dict = GetVotesResponse.from_dict(get_votes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


