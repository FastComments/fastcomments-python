# SetTrustFactorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**previous_manual_trust_factor** | **float** |  | [optional] 
**status** | [**APIStatus**](APIStatus.md) |  | 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.set_trust_factor_response import SetTrustFactorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SetTrustFactorResponse from a JSON string
set_trust_factor_response_instance = SetTrustFactorResponse.from_json(json)
# print the JSON string representation of the object
print(SetTrustFactorResponse.to_json())

# convert the object into a dict
set_trust_factor_response_dict = set_trust_factor_response_instance.to_dict()
# create an instance of SetTrustFactorResponse from a dict
set_trust_factor_response_from_dict = SetTrustFactorResponse.from_dict(set_trust_factor_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


