# PatchDomainConfigParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** |  | [optional] 
**email_from_name** | **str** |  | [optional] 
**email_from_email** | **str** |  | [optional] 
**logo_src** | **str** |  | [optional] 
**logo_src100px** | **str** |  | [optional] 
**footer_unsubscribe_url** | **str** |  | [optional] 
**email_headers** | **Dict[str, str]** | Construct a type with a set of properties K of type T | [optional] 

## Example

```python
from client.models.patch_domain_config_params import PatchDomainConfigParams

# TODO update the JSON string below
json = "{}"
# create an instance of PatchDomainConfigParams from a JSON string
patch_domain_config_params_instance = PatchDomainConfigParams.from_json(json)
# print the JSON string representation of the object
print(PatchDomainConfigParams.to_json())

# convert the object into a dict
patch_domain_config_params_dict = patch_domain_config_params_instance.to_dict()
# create an instance of PatchDomainConfigParams from a dict
patch_domain_config_params_from_dict = PatchDomainConfigParams.from_dict(patch_domain_config_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


