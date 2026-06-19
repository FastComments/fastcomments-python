# BanUserUndoParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changelog** | [**APIBanUserChangeLog**](APIBanUserChangeLog.md) |  | 

## Example

```python
from client.models.ban_user_undo_params import BanUserUndoParams

# TODO update the JSON string below
json = "{}"
# create an instance of BanUserUndoParams from a JSON string
ban_user_undo_params_instance = BanUserUndoParams.from_json(json)
# print the JSON string representation of the object
print(BanUserUndoParams.to_json())

# convert the object into a dict
ban_user_undo_params_dict = ban_user_undo_params_instance.to_dict()
# create an instance of BanUserUndoParams from a dict
ban_user_undo_params_from_dict = BanUserUndoParams.from_dict(ban_user_undo_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


