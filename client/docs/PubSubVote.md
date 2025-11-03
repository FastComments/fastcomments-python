# PubSubVote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**url_id** | **str** |  | 
**url_id_raw** | **str** |  | 
**comment_id** | **str** |  | 
**user_id** | **str** |  | [optional] 
**direction** | **int** |  | 
**created_at** | **int** |  | 
**verification_id** | **str** |  | 

## Example

```python
from generated.models.pub_sub_vote import PubSubVote

# TODO update the JSON string below
json = "{}"
# create an instance of PubSubVote from a JSON string
pub_sub_vote_instance = PubSubVote.from_json(json)
# print the JSON string representation of the object
print(PubSubVote.to_json())

# convert the object into a dict
pub_sub_vote_dict = pub_sub_vote_instance.to_dict()
# create an instance of PubSubVote from a dict
pub_sub_vote_from_dict = PubSubVote.from_dict(pub_sub_vote_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


