# GetDomainConfigsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configurations** | **object** |  | 
**status** | **object** |  | 
**reason** | **str** |  | 
**code** | **str** |  | 

## Example

```python
from client.models.get_domain_configs_response import GetDomainConfigsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDomainConfigsResponse from a JSON string
get_domain_configs_response_instance = GetDomainConfigsResponse.from_json(json)
# print the JSON string representation of the object
print(GetDomainConfigsResponse.to_json())

# convert the object into a dict
get_domain_configs_response_dict = get_domain_configs_response_instance.to_dict()
# create an instance of GetDomainConfigsResponse from a dict
get_domain_configs_response_from_dict = GetDomainConfigsResponse.from_dict(get_domain_configs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


