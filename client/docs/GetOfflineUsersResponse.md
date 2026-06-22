# GetOfflineUsersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_after_user_id** | **str** |  | 
**next_after_name** | **str** |  | 
**users** | [**List[PageUserEntry]**](PageUserEntry.md) |  | 
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
from client.models.get_offline_users_response import GetOfflineUsersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetOfflineUsersResponse from a JSON string
get_offline_users_response_instance = GetOfflineUsersResponse.from_json(json)
# print the JSON string representation of the object
print(GetOfflineUsersResponse.to_json())

# convert the object into a dict
get_offline_users_response_dict = get_offline_users_response_instance.to_dict()
# create an instance of GetOfflineUsersResponse from a dict
get_offline_users_response_from_dict = GetOfflineUsersResponse.from_dict(get_offline_users_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


