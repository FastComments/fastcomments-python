# GetEmailTemplateDefinitionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**definitions** | [**List[EmailTemplateDefinition]**](EmailTemplateDefinition.md) |  | 

## Example

```python
from client.models.get_email_template_definitions_response import GetEmailTemplateDefinitionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetEmailTemplateDefinitionsResponse from a JSON string
get_email_template_definitions_response_instance = GetEmailTemplateDefinitionsResponse.from_json(json)
# print the JSON string representation of the object
print(GetEmailTemplateDefinitionsResponse.to_json())

# convert the object into a dict
get_email_template_definitions_response_dict = get_email_template_definitions_response_instance.to_dict()
# create an instance of GetEmailTemplateDefinitionsResponse from a dict
get_email_template_definitions_response_from_dict = GetEmailTemplateDefinitionsResponse.from_dict(get_email_template_definitions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


