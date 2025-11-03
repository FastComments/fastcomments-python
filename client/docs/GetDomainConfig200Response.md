# GetDomainConfig200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration** | **object** |  | 
**status** | **object** |  | 
**reason** | **str** |  | 
**code** | **str** |  | 

## Example

```python
from client.models.get_domain_config200_response import GetDomainConfig200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDomainConfig200Response from a JSON string
get_domain_config200_response_instance = GetDomainConfig200Response.from_json(json)
# print the JSON string representation of the object
print(GetDomainConfig200Response.to_json())

# convert the object into a dict
get_domain_config200_response_dict = get_domain_config200_response_instance.to_dict()
# create an instance of GetDomainConfig200Response from a dict
get_domain_config200_response_from_dict = GetDomainConfig200Response.from_dict(get_domain_config200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


