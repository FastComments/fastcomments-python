# PutDomainConfigResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration** | **object** |  | [optional] 
**status** | **object** |  | 
**reason** | **str** |  | [optional] 
**code** | **str** |  | [optional] 

## Example

```python
from client.models.put_domain_config_response import PutDomainConfigResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutDomainConfigResponse from a JSON string
put_domain_config_response_instance = PutDomainConfigResponse.from_json(json)
# print the JSON string representation of the object
print(PutDomainConfigResponse.to_json())

# convert the object into a dict
put_domain_config_response_dict = put_domain_config_response_instance.to_dict()
# create an instance of PutDomainConfigResponse from a dict
put_domain_config_response_from_dict = PutDomainConfigResponse.from_dict(put_domain_config_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


