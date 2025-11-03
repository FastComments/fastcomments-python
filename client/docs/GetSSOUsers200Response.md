# GetSSOUsers200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[APISSOUser]**](APISSOUser.md) |  | 
**status** | **str** |  | 

## Example

```python
from client.models.get_sso_users200_response import GetSSOUsers200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSSOUsers200Response from a JSON string
get_sso_users200_response_instance = GetSSOUsers200Response.from_json(json)
# print the JSON string representation of the object
print(GetSSOUsers200Response.to_json())

# convert the object into a dict
get_sso_users200_response_dict = get_sso_users200_response_instance.to_dict()
# create an instance of GetSSOUsers200Response from a dict
get_sso_users200_response_from_dict = GetSSOUsers200Response.from_dict(get_sso_users200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


