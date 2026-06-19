# GetV2PageReactUsersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_names** | **List[str]** |  | 
**status** | [**APIStatus**](APIStatus.md) |  | 

## Example

```python
from client.models.get_v2_page_react_users_response import GetV2PageReactUsersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetV2PageReactUsersResponse from a JSON string
get_v2_page_react_users_response_instance = GetV2PageReactUsersResponse.from_json(json)
# print the JSON string representation of the object
print(GetV2PageReactUsersResponse.to_json())

# convert the object into a dict
get_v2_page_react_users_response_dict = get_v2_page_react_users_response_instance.to_dict()
# create an instance of GetV2PageReactUsersResponse from a dict
get_v2_page_react_users_response_from_dict = GetV2PageReactUsersResponse.from_dict(get_v2_page_react_users_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


