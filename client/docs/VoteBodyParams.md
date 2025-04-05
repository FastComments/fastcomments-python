# VoteBodyParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commenter_email** | **str** |  | 
**commenter_name** | **str** |  | 
**vote_dir** | **str** |  | 
**url** | **str** |  | 

## Example

```python
from openapi_client.models.vote_body_params import VoteBodyParams

# TODO update the JSON string below
json = "{}"
# create an instance of VoteBodyParams from a JSON string
vote_body_params_instance = VoteBodyParams.from_json(json)
# print the JSON string representation of the object
print(VoteBodyParams.to_json())

# convert the object into a dict
vote_body_params_dict = vote_body_params_instance.to_dict()
# create an instance of VoteBodyParams from a dict
vote_body_params_from_dict = VoteBodyParams.from_dict(vote_body_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


