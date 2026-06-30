# SearchUsersResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**sections** | [**List[UserSearchSectionResult]**](UserSearchSectionResult.md) |  | [optional] 
**users** | [**List[UserSearchResult]**](UserSearchResult.md) |  | [optional] 

## Example

```python
from client.models.search_users_result import SearchUsersResult

# TODO update the JSON string below
json = "{}"
# create an instance of SearchUsersResult from a JSON string
search_users_result_instance = SearchUsersResult.from_json(json)
# print the JSON string representation of the object
print(SearchUsersResult.to_json())

# convert the object into a dict
search_users_result_dict = search_users_result_instance.to_dict()
# create an instance of SearchUsersResult from a dict
search_users_result_from_dict = SearchUsersResult.from_dict(search_users_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


