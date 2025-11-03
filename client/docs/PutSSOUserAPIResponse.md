# PutSSOUserAPIResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**user** | [**APISSOUser**](APISSOUser.md) |  | [optional] 
**status** | **str** |  | 

## Example

```python
from generated.models.put_sso_user_api_response import PutSSOUserAPIResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutSSOUserAPIResponse from a JSON string
put_sso_user_api_response_instance = PutSSOUserAPIResponse.from_json(json)
# print the JSON string representation of the object
print(PutSSOUserAPIResponse.to_json())

# convert the object into a dict
put_sso_user_api_response_dict = put_sso_user_api_response_instance.to_dict()
# create an instance of PutSSOUserAPIResponse from a dict
put_sso_user_api_response_from_dict = PutSSOUserAPIResponse.from_dict(put_sso_user_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


