# PatchDomainConfigResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration** | **object** |  | 
**status** | **object** |  | 
**reason** | **str** |  | 
**code** | **str** |  | 

## Example

```python
from client.models.patch_domain_config_response import PatchDomainConfigResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PatchDomainConfigResponse from a JSON string
patch_domain_config_response_instance = PatchDomainConfigResponse.from_json(json)
# print the JSON string representation of the object
print(PatchDomainConfigResponse.to_json())

# convert the object into a dict
patch_domain_config_response_dict = patch_domain_config_response_instance.to_dict()
# create an instance of PatchDomainConfigResponse from a dict
patch_domain_config_response_from_dict = PatchDomainConfigResponse.from_dict(patch_domain_config_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


