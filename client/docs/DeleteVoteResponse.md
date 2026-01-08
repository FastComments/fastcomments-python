# DeleteVoteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 

## Example

```python
from client.models.delete_vote_response import DeleteVoteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteVoteResponse from a JSON string
delete_vote_response_instance = DeleteVoteResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteVoteResponse.to_json())

# convert the object into a dict
delete_vote_response_dict = delete_vote_response_instance.to_dict()
# create an instance of DeleteVoteResponse from a dict
delete_vote_response_from_dict = DeleteVoteResponse.from_dict(delete_vote_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


