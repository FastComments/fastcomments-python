# GetOnlineUsersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_after_user_id** | **str** |  | 
**next_after_name** | **str** |  | 
**total_count** | **float** |  | 
**anon_count** | **float** |  | 
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
from client.models.get_online_users_response import GetOnlineUsersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetOnlineUsersResponse from a JSON string
get_online_users_response_instance = GetOnlineUsersResponse.from_json(json)
# print the JSON string representation of the object
print(GetOnlineUsersResponse.to_json())

# convert the object into a dict
get_online_users_response_dict = get_online_users_response_instance.to_dict()
# create an instance of GetOnlineUsersResponse from a dict
get_online_users_response_from_dict = GetOnlineUsersResponse.from_dict(get_online_users_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


