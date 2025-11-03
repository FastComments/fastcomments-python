# VoteResponseUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** |  | [optional] 

## Example

```python
from client.models.vote_response_user import VoteResponseUser

# TODO update the JSON string below
json = "{}"
# create an instance of VoteResponseUser from a JSON string
vote_response_user_instance = VoteResponseUser.from_json(json)
# print the JSON string representation of the object
print(VoteResponseUser.to_json())

# convert the object into a dict
vote_response_user_dict = vote_response_user_instance.to_dict()
# create an instance of VoteResponseUser from a dict
vote_response_user_from_dict = VoteResponseUser.from_dict(vote_response_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


