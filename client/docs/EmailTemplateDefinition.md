# EmailTemplateDefinition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_template_id** | **str** |  | 
**default_test_data** | **Dict[str, object]** | Construct a type with a set of properties K of type T | 
**default_translations_by_locale** | **Dict[str, Dict[str, str]]** | Construct a type with a set of properties K of type T | 
**default_ejs** | **str** |  | 

## Example

```python
from client.models.email_template_definition import EmailTemplateDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of EmailTemplateDefinition from a JSON string
email_template_definition_instance = EmailTemplateDefinition.from_json(json)
# print the JSON string representation of the object
print(EmailTemplateDefinition.to_json())

# convert the object into a dict
email_template_definition_dict = email_template_definition_instance.to_dict()
# create an instance of EmailTemplateDefinition from a dict
email_template_definition_from_dict = EmailTemplateDefinition.from_dict(email_template_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


