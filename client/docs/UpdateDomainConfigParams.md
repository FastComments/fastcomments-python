# UpdateDomainConfigParams


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
from client.models.update_domain_config_params import UpdateDomainConfigParams

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDomainConfigParams from a JSON string
update_domain_config_params_instance = UpdateDomainConfigParams.from_json(json)
# print the JSON string representation of the object
print(UpdateDomainConfigParams.to_json())

# convert the object into a dict
update_domain_config_params_dict = update_domain_config_params_instance.to_dict()
# create an instance of UpdateDomainConfigParams from a dict
update_domain_config_params_from_dict = UpdateDomainConfigParams.from_dict(update_domain_config_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


