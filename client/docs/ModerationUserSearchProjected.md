# ModerationUserSearchProjected


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**username** | **str** |  | 
**display_name** | **str** |  | [optional] 
**avatar_src** | **str** |  | [optional] 

## Example

```python
from client.models.moderation_user_search_projected import ModerationUserSearchProjected

# TODO update the JSON string below
json = "{}"
# create an instance of ModerationUserSearchProjected from a JSON string
moderation_user_search_projected_instance = ModerationUserSearchProjected.from_json(json)
# print the JSON string representation of the object
print(ModerationUserSearchProjected.to_json())

# convert the object into a dict
moderation_user_search_projected_dict = moderation_user_search_projected_instance.to_dict()
# create an instance of ModerationUserSearchProjected from a dict
moderation_user_search_projected_from_dict = ModerationUserSearchProjected.from_dict(moderation_user_search_projected_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


