# CreateUserBadgeParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**badge_id** | **str** |  | 
**displayed_on_comments** | **bool** |  | [optional] 

## Example

```python
from client.models.create_user_badge_params import CreateUserBadgeParams

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserBadgeParams from a JSON string
create_user_badge_params_instance = CreateUserBadgeParams.from_json(json)
# print the JSON string representation of the object
print(CreateUserBadgeParams.to_json())

# convert the object into a dict
create_user_badge_params_dict = create_user_badge_params_instance.to_dict()
# create an instance of CreateUserBadgeParams from a dict
create_user_badge_params_from_dict = CreateUserBadgeParams.from_dict(create_user_badge_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


