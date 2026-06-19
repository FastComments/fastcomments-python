# GetUserTrustFactorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manual_trust_factor** | **float** |  | [optional] 
**auto_trust_factor** | **float** |  | [optional] 
**status** | [**APIStatus**](APIStatus.md) |  | 

## Example

```python
from client.models.get_user_trust_factor_response import GetUserTrustFactorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserTrustFactorResponse from a JSON string
get_user_trust_factor_response_instance = GetUserTrustFactorResponse.from_json(json)
# print the JSON string representation of the object
print(GetUserTrustFactorResponse.to_json())

# convert the object into a dict
get_user_trust_factor_response_dict = get_user_trust_factor_response_instance.to_dict()
# create an instance of GetUserTrustFactorResponse from a dict
get_user_trust_factor_response_from_dict = GetUserTrustFactorResponse.from_dict(get_user_trust_factor_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


