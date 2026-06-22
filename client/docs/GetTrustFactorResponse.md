# GetTrustFactorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manual_trust_factor** | **float** |  | [optional] 
**auto_trust_factor** | **float** |  | [optional] 
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
from client.models.get_trust_factor_response import GetTrustFactorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTrustFactorResponse from a JSON string
get_trust_factor_response_instance = GetTrustFactorResponse.from_json(json)
# print the JSON string representation of the object
print(GetTrustFactorResponse.to_json())

# convert the object into a dict
get_trust_factor_response_dict = get_trust_factor_response_instance.to_dict()
# create an instance of GetTrustFactorResponse from a dict
get_trust_factor_response_from_dict = GetTrustFactorResponse.from_dict(get_trust_factor_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


