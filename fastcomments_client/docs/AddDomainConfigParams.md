# AddDomainConfigParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** |  | 
**email_from_name** | **str** |  | [optional] 
**email_from_email** | **str** |  | [optional] 
**logo_src** | **str** |  | [optional] 
**logo_src100px** | **str** |  | [optional] 
**footer_unsubscribe_url** | **str** |  | [optional] 
**email_headers** | **Dict[str, str]** | Construct a type with a set of properties K of type T | [optional] 

## Example

```python
from openapi_client.models.add_domain_config_params import AddDomainConfigParams

# TODO update the JSON string below
json = "{}"
# create an instance of AddDomainConfigParams from a JSON string
add_domain_config_params_instance = AddDomainConfigParams.from_json(json)
# print the JSON string representation of the object
print(AddDomainConfigParams.to_json())

# convert the object into a dict
add_domain_config_params_dict = add_domain_config_params_instance.to_dict()
# create an instance of AddDomainConfigParams from a dict
add_domain_config_params_from_dict = AddDomainConfigParams.from_dict(add_domain_config_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


