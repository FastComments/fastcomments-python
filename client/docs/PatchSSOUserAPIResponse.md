# PatchSSOUserAPIResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**user** | [**APISSOUser**](APISSOUser.md) |  | [optional] 
**status** | **str** |  | 

## Example

```python
from generated.models.patch_sso_user_api_response import PatchSSOUserAPIResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PatchSSOUserAPIResponse from a JSON string
patch_sso_user_api_response_instance = PatchSSOUserAPIResponse.from_json(json)
# print the JSON string representation of the object
print(PatchSSOUserAPIResponse.to_json())

# convert the object into a dict
patch_sso_user_api_response_dict = patch_sso_user_api_response_instance.to_dict()
# create an instance of PatchSSOUserAPIResponse from a dict
patch_sso_user_api_response_from_dict = PatchSSOUserAPIResponse.from_dict(patch_sso_user_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


