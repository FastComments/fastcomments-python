# PostBanUserUndoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.post_ban_user_undo_response import PostBanUserUndoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostBanUserUndoResponse from a JSON string
post_ban_user_undo_response_instance = PostBanUserUndoResponse.from_json(json)
# print the JSON string representation of the object
print(PostBanUserUndoResponse.to_json())

# convert the object into a dict
post_ban_user_undo_response_dict = post_ban_user_undo_response_instance.to_dict()
# create an instance of PostBanUserUndoResponse from a dict
post_ban_user_undo_response_from_dict = PostBanUserUndoResponse.from_dict(post_ban_user_undo_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


