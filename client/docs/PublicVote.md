# PublicVote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**url_id** | **str** |  | 
**comment_id** | **str** |  | 
**user_id** | **str** |  | 
**direction** | **str** |  | 
**created_at** | **datetime** |  | 

## Example

```python
from client.models.public_vote import PublicVote

# TODO update the JSON string below
json = "{}"
# create an instance of PublicVote from a JSON string
public_vote_instance = PublicVote.from_json(json)
# print the JSON string representation of the object
print(PublicVote.to_json())

# convert the object into a dict
public_vote_dict = public_vote_instance.to_dict()
# create an instance of PublicVote from a dict
public_vote_from_dict = PublicVote.from_dict(public_vote_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


