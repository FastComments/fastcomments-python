# AddSSOUserAPIResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**user** | [**APISSOUser**](APISSOUser.md) |  | [optional] 
**status** | **str** |  | 

## Example

```python
from generated.models.add_sso_user_api_response import AddSSOUserAPIResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddSSOUserAPIResponse from a JSON string
add_sso_user_api_response_instance = AddSSOUserAPIResponse.from_json(json)
# print the JSON string representation of the object
print(AddSSOUserAPIResponse.to_json())

# convert the object into a dict
add_sso_user_api_response_dict = add_sso_user_api_response_instance.to_dict()
# create an instance of AddSSOUserAPIResponse from a dict
add_sso_user_api_response_from_dict = AddSSOUserAPIResponse.from_dict(add_sso_user_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


