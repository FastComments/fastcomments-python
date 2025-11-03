# AddDomainConfig200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | 
**code** | **str** |  | 
**status** | **object** |  | 
**configuration** | **object** |  | 

## Example

```python
from client.models.add_domain_config200_response import AddDomainConfig200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AddDomainConfig200Response from a JSON string
add_domain_config200_response_instance = AddDomainConfig200Response.from_json(json)
# print the JSON string representation of the object
print(AddDomainConfig200Response.to_json())

# convert the object into a dict
add_domain_config200_response_dict = add_domain_config200_response_instance.to_dict()
# create an instance of AddDomainConfig200Response from a dict
add_domain_config200_response_from_dict = AddDomainConfig200Response.from_dict(add_domain_config200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


