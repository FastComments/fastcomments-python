# GetSSOUserByIdAPIResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**user** | [**APISSOUser**](APISSOUser.md) |  | [optional] 
**status** | **str** |  | 

## Example

```python
from generated.models.get_sso_user_by_id_api_response import GetSSOUserByIdAPIResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSSOUserByIdAPIResponse from a JSON string
get_sso_user_by_id_api_response_instance = GetSSOUserByIdAPIResponse.from_json(json)
# print the JSON string representation of the object
print(GetSSOUserByIdAPIResponse.to_json())

# convert the object into a dict
get_sso_user_by_id_api_response_dict = get_sso_user_by_id_api_response_instance.to_dict()
# create an instance of GetSSOUserByIdAPIResponse from a dict
get_sso_user_by_id_api_response_from_dict = GetSSOUserByIdAPIResponse.from_dict(get_sso_user_by_id_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


