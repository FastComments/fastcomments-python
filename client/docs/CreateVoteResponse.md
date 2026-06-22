# CreateVoteResponse


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
from client.models.create_vote_response import CreateVoteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateVoteResponse from a JSON string
create_vote_response_instance = CreateVoteResponse.from_json(json)
# print the JSON string representation of the object
print(CreateVoteResponse.to_json())

# convert the object into a dict
create_vote_response_dict = create_vote_response_instance.to_dict()
# create an instance of CreateVoteResponse from a dict
create_vote_response_from_dict = CreateVoteResponse.from_dict(create_vote_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


