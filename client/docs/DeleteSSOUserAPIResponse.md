# DeleteSSOUserAPIResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**user** | [**APISSOUser**](APISSOUser.md) |  | [optional] 
**status** | **str** |  | 

## Example

```python
from generated.models.delete_sso_user_api_response import DeleteSSOUserAPIResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteSSOUserAPIResponse from a JSON string
delete_sso_user_api_response_instance = DeleteSSOUserAPIResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteSSOUserAPIResponse.to_json())

# convert the object into a dict
delete_sso_user_api_response_dict = delete_sso_user_api_response_instance.to_dict()
# create an instance of DeleteSSOUserAPIResponse from a dict
delete_sso_user_api_response_from_dict = DeleteSSOUserAPIResponse.from_dict(delete_sso_user_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


