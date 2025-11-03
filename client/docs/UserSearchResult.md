# UserSearchResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**display_name** | **str** |  | [optional] 
**avatar_src** | **str** |  | [optional] 
**type** | **str** |  | 

## Example

```python
from generated.models.user_search_result import UserSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of UserSearchResult from a JSON string
user_search_result_instance = UserSearchResult.from_json(json)
# print the JSON string representation of the object
print(UserSearchResult.to_json())

# convert the object into a dict
user_search_result_dict = user_search_result_instance.to_dict()
# create an instance of UserSearchResult from a dict
user_search_result_from_dict = UserSearchResult.from_dict(user_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


