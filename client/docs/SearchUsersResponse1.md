# SearchUsersResponse1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**sections** | [**List[UserSearchSectionResult]**](UserSearchSectionResult.md) |  | 
**users** | [**List[UserSearchResult]**](UserSearchResult.md) |  | 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.search_users_response1 import SearchUsersResponse1

# TODO update the JSON string below
json = "{}"
# create an instance of SearchUsersResponse1 from a JSON string
search_users_response1_instance = SearchUsersResponse1.from_json(json)
# print the JSON string representation of the object
print(SearchUsersResponse1.to_json())

# convert the object into a dict
search_users_response1_dict = search_users_response1_instance.to_dict()
# create an instance of SearchUsersResponse1 from a dict
search_users_response1_from_dict = SearchUsersResponse1.from_dict(search_users_response1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


