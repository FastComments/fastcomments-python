# CreateEmailTemplateBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_template_id** | **str** |  | 
**display_name** | **str** |  | 
**ejs** | **str** |  | 
**domain** | **str** |  | [optional] 
**translation_overrides_by_locale** | **Dict[str, Dict[str, str]]** | Construct a type with a set of properties K of type T | [optional] 
**test_data** | **Dict[str, object]** | Construct a type with a set of properties K of type T | [optional] 

## Example

```python
from client.models.create_email_template_body import CreateEmailTemplateBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEmailTemplateBody from a JSON string
create_email_template_body_instance = CreateEmailTemplateBody.from_json(json)
# print the JSON string representation of the object
print(CreateEmailTemplateBody.to_json())

# convert the object into a dict
create_email_template_body_dict = create_email_template_body_instance.to_dict()
# create an instance of CreateEmailTemplateBody from a dict
create_email_template_body_from_dict = CreateEmailTemplateBody.from_dict(create_email_template_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


