# CreateModeratorBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**email** | **str** |  | 
**user_id** | **str** |  | [optional] 
**moderation_group_ids** | **List[str]** |  | [optional] 

## Example

```python
from client.models.create_moderator_body import CreateModeratorBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreateModeratorBody from a JSON string
create_moderator_body_instance = CreateModeratorBody.from_json(json)
# print the JSON string representation of the object
print(CreateModeratorBody.to_json())

# convert the object into a dict
create_moderator_body_dict = create_moderator_body_instance.to_dict()
# create an instance of CreateModeratorBody from a dict
create_moderator_body_from_dict = CreateModeratorBody.from_dict(create_moderator_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


