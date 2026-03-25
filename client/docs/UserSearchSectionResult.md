# UserSearchSectionResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**section** | [**UserSearchSection**](UserSearchSection.md) |  | 
**users** | [**List[UserSearchResult]**](UserSearchResult.md) |  | 

## Example

```python
from client.models.user_search_section_result import UserSearchSectionResult

# TODO update the JSON string below
json = "{}"
# create an instance of UserSearchSectionResult from a JSON string
user_search_section_result_instance = UserSearchSectionResult.from_json(json)
# print the JSON string representation of the object
print(UserSearchSectionResult.to_json())

# convert the object into a dict
user_search_section_result_dict = user_search_section_result_instance.to_dict()
# create an instance of UserSearchSectionResult from a dict
user_search_section_result_from_dict = UserSearchSectionResult.from_dict(user_search_section_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


