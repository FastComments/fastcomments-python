# GetEmailTemplateDefinitionsResponse1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**definitions** | [**List[EmailTemplateDefinition]**](EmailTemplateDefinition.md) |  | 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.get_email_template_definitions_response1 import GetEmailTemplateDefinitionsResponse1

# TODO update the JSON string below
json = "{}"
# create an instance of GetEmailTemplateDefinitionsResponse1 from a JSON string
get_email_template_definitions_response1_instance = GetEmailTemplateDefinitionsResponse1.from_json(json)
# print the JSON string representation of the object
print(GetEmailTemplateDefinitionsResponse1.to_json())

# convert the object into a dict
get_email_template_definitions_response1_dict = get_email_template_definitions_response1_instance.to_dict()
# create an instance of GetEmailTemplateDefinitionsResponse1 from a dict
get_email_template_definitions_response1_from_dict = GetEmailTemplateDefinitionsResponse1.from_dict(get_email_template_definitions_response1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


