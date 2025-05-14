# VoteDeleteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**VoteDeleteResponseStatus**](VoteDeleteResponseStatus.md) |  | 
**was_pending_vote** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.vote_delete_response import VoteDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VoteDeleteResponse from a JSON string
vote_delete_response_instance = VoteDeleteResponse.from_json(json)
# print the JSON string representation of the object
print(VoteDeleteResponse.to_json())

# convert the object into a dict
vote_delete_response_dict = vote_delete_response_instance.to_dict()
# create an instance of VoteDeleteResponse from a dict
vote_delete_response_from_dict = VoteDeleteResponse.from_dict(vote_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


