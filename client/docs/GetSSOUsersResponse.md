# GetSSOUsersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[APISSOUser]**](APISSOUser.md) |  | 
**status** | **str** |  | 

## Example

```python
from client.models.get_sso_users_response import GetSSOUsersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSSOUsersResponse from a JSON string
get_sso_users_response_instance = GetSSOUsersResponse.from_json(json)
# print the JSON string representation of the object
print(GetSSOUsersResponse.to_json())

# convert the object into a dict
get_sso_users_response_dict = get_sso_users_response_instance.to_dict()
# create an instance of GetSSOUsersResponse from a dict
get_sso_users_response_from_dict = GetSSOUsersResponse.from_dict(get_sso_users_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


