# SearchUsersSectionedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**sections** | [**List[UserSearchSectionResult]**](UserSearchSectionResult.md) |  | 

## Example

```python
from client.models.search_users_sectioned_response import SearchUsersSectionedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SearchUsersSectionedResponse from a JSON string
search_users_sectioned_response_instance = SearchUsersSectionedResponse.from_json(json)
# print the JSON string representation of the object
print(SearchUsersSectionedResponse.to_json())

# convert the object into a dict
search_users_sectioned_response_dict = search_users_sectioned_response_instance.to_dict()
# create an instance of SearchUsersSectionedResponse from a dict
search_users_sectioned_response_from_dict = SearchUsersSectionedResponse.from_dict(search_users_sectioned_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


