# APIDomainConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**domain** | **str** |  | 
**email_from_name** | **str** |  | [optional] 
**email_from_email** | **str** |  | [optional] 
**email_headers** | **Dict[str, str]** | Construct a type with a set of properties K of type T | [optional] 
**wp_sync_token** | **str** |  | [optional] 
**wp_synced** | **bool** |  | [optional] 
**wp_url** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**auto_added_date** | **datetime** |  | [optional] 
**site_type** | [**ImportedSiteType**](ImportedSiteType.md) |  | [optional] 
**logo_src** | **str** |  | [optional] 
**logo_src100px** | **str** |  | [optional] 
**footer_unsubscribe_url** | **str** |  | [optional] 
**disable_unsubscribe_links** | **bool** |  | [optional] 

## Example

```python
from client.models.api_domain_configuration import APIDomainConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of APIDomainConfiguration from a JSON string
api_domain_configuration_instance = APIDomainConfiguration.from_json(json)
# print the JSON string representation of the object
print(APIDomainConfiguration.to_json())

# convert the object into a dict
api_domain_configuration_dict = api_domain_configuration_instance.to_dict()
# create an instance of APIDomainConfiguration from a dict
api_domain_configuration_from_dict = APIDomainConfiguration.from_dict(api_domain_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


