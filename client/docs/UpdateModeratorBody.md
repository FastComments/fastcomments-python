# UpdateModeratorBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**moderation_group_ids** | **List[str]** |  | [optional] 

## Example

```python
from client.models.update_moderator_body import UpdateModeratorBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateModeratorBody from a JSON string
update_moderator_body_instance = UpdateModeratorBody.from_json(json)
# print the JSON string representation of the object
print(UpdateModeratorBody.to_json())

# convert the object into a dict
update_moderator_body_dict = update_moderator_body_instance.to_dict()
# create an instance of UpdateModeratorBody from a dict
update_moderator_body_from_dict = UpdateModeratorBody.from_dict(update_moderator_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


