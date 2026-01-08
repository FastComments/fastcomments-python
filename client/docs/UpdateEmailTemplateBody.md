# UpdateEmailTemplateBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_template_id** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**ejs** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 
**translation_overrides_by_locale** | **Dict[str, Dict[str, str]]** | Construct a type with a set of properties K of type T | [optional] 
**test_data** | **Dict[str, object]** | Construct a type with a set of properties K of type T | [optional] 

## Example

```python
from client.models.update_email_template_body import UpdateEmailTemplateBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateEmailTemplateBody from a JSON string
update_email_template_body_instance = UpdateEmailTemplateBody.from_json(json)
# print the JSON string representation of the object
print(UpdateEmailTemplateBody.to_json())

# convert the object into a dict
update_email_template_body_dict = update_email_template_body_instance.to_dict()
# create an instance of UpdateEmailTemplateBody from a dict
update_email_template_body_from_dict = UpdateEmailTemplateBody.from_dict(update_email_template_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


