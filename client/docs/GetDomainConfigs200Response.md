# GetDomainConfigs200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configurations** | **object** |  | 
**status** | **object** |  | 
**reason** | **str** |  | 
**code** | **str** |  | 

## Example

```python
from generated.models.get_domain_configs200_response import GetDomainConfigs200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDomainConfigs200Response from a JSON string
get_domain_configs200_response_instance = GetDomainConfigs200Response.from_json(json)
# print the JSON string representation of the object
print(GetDomainConfigs200Response.to_json())

# convert the object into a dict
get_domain_configs200_response_dict = get_domain_configs200_response_instance.to_dict()
# create an instance of GetDomainConfigs200Response from a dict
get_domain_configs200_response_from_dict = GetDomainConfigs200Response.from_dict(get_domain_configs200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


