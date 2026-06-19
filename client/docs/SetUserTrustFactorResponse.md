# SetUserTrustFactorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**previous_manual_trust_factor** | **float** |  | [optional] 
**status** | [**APIStatus**](APIStatus.md) |  | 

## Example

```python
from client.models.set_user_trust_factor_response import SetUserTrustFactorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SetUserTrustFactorResponse from a JSON string
set_user_trust_factor_response_instance = SetUserTrustFactorResponse.from_json(json)
# print the JSON string representation of the object
print(SetUserTrustFactorResponse.to_json())

# convert the object into a dict
set_user_trust_factor_response_dict = set_user_trust_factor_response_instance.to_dict()
# create an instance of SetUserTrustFactorResponse from a dict
set_user_trust_factor_response_from_dict = SetUserTrustFactorResponse.from_dict(set_user_trust_factor_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


