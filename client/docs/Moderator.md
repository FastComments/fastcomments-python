# Moderator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**name** | **str** |  | 
**user_id** | **str** |  | 
**accepted_invite** | **bool** |  | 
**email** | **str** |  | 
**mark_reviewed_count** | **float** |  | 
**deleted_count** | **float** |  | 
**marked_spam_count** | **float** |  | 
**marked_not_spam_count** | **float** |  | 
**approved_count** | **float** |  | 
**un_approved_count** | **float** |  | 
**edited_count** | **float** |  | 
**banned_count** | **float** |  | 
**un_flagged_count** | **float** |  | 
**verification_id** | **str** |  | 
**created_at** | **datetime** |  | 
**moderation_group_ids** | **List[str]** |  | 

## Example

```python
from client.models.moderator import Moderator

# TODO update the JSON string below
json = "{}"
# create an instance of Moderator from a JSON string
moderator_instance = Moderator.from_json(json)
# print the JSON string representation of the object
print(Moderator.to_json())

# convert the object into a dict
moderator_dict = moderator_instance.to_dict()
# create an instance of Moderator from a dict
moderator_from_dict = Moderator.from_dict(moderator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


