# GetSearchUsersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[ModerationUserSearchProjected]**](ModerationUserSearchProjected.md) |  | 
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
from client.models.get_search_users_response import GetSearchUsersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSearchUsersResponse from a JSON string
get_search_users_response_instance = GetSearchUsersResponse.from_json(json)
# print the JSON string representation of the object
print(GetSearchUsersResponse.to_json())

# convert the object into a dict
get_search_users_response_dict = get_search_users_response_instance.to_dict()
# create an instance of GetSearchUsersResponse from a dict
get_search_users_response_from_dict = GetSearchUsersResponse.from_dict(get_search_users_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


