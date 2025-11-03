# VoteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**VoteResponseStatus**](VoteResponseStatus.md) |  | 
**vote_id** | **str** |  | [optional] 
**is_verified** | **bool** |  | [optional] 
**user** | [**VoteResponseUser**](VoteResponseUser.md) |  | [optional] 
**edit_key** | **str** |  | [optional] 

## Example

```python
from generated.models.vote_response import VoteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VoteResponse from a JSON string
vote_response_instance = VoteResponse.from_json(json)
# print the JSON string representation of the object
print(VoteResponse.to_json())

# convert the object into a dict
vote_response_dict = vote_response_instance.to_dict()
# create an instance of VoteResponse from a dict
vote_response_from_dict = VoteResponse.from_dict(vote_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


