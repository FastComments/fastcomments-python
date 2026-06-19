# AdjustVotesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**new_comment_votes** | **int** |  | 

## Example

```python
from client.models.adjust_votes_response import AdjustVotesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AdjustVotesResponse from a JSON string
adjust_votes_response_instance = AdjustVotesResponse.from_json(json)
# print the JSON string representation of the object
print(AdjustVotesResponse.to_json())

# convert the object into a dict
adjust_votes_response_dict = adjust_votes_response_instance.to_dict()
# create an instance of AdjustVotesResponse from a dict
adjust_votes_response_from_dict = AdjustVotesResponse.from_dict(adjust_votes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


