# AddDomainConfigResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**status** | **object** |  | 
**configuration** | **object** |  | [optional] 

## Example

```python
from client.models.add_domain_config_response import AddDomainConfigResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddDomainConfigResponse from a JSON string
add_domain_config_response_instance = AddDomainConfigResponse.from_json(json)
# print the JSON string representation of the object
print(AddDomainConfigResponse.to_json())

# convert the object into a dict
add_domain_config_response_dict = add_domain_config_response_instance.to_dict()
# create an instance of AddDomainConfigResponse from a dict
add_domain_config_response_from_dict = AddDomainConfigResponse.from_dict(add_domain_config_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


