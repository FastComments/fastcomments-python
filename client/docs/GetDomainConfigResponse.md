# GetDomainConfigResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration** | **object** |  | [optional] 
**status** | **object** |  | 
**reason** | **str** |  | [optional] 
**code** | **str** |  | [optional] 

## Example

```python
from client.models.get_domain_config_response import GetDomainConfigResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDomainConfigResponse from a JSON string
get_domain_config_response_instance = GetDomainConfigResponse.from_json(json)
# print the JSON string representation of the object
print(GetDomainConfigResponse.to_json())

# convert the object into a dict
get_domain_config_response_dict = get_domain_config_response_instance.to_dict()
# create an instance of GetDomainConfigResponse from a dict
get_domain_config_response_from_dict = GetDomainConfigResponse.from_dict(get_domain_config_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


