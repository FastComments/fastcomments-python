# RenderEmailTemplateBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_template_id** | **str** |  | 
**ejs** | **str** |  | 
**test_data** | **Dict[str, object]** | Construct a type with a set of properties K of type T | [optional] 
**translation_overrides_by_locale** | **Dict[str, Dict[str, str]]** | Construct a type with a set of properties K of type T | [optional] 

## Example

```python
from client.models.render_email_template_body import RenderEmailTemplateBody

# TODO update the JSON string below
json = "{}"
# create an instance of RenderEmailTemplateBody from a JSON string
render_email_template_body_instance = RenderEmailTemplateBody.from_json(json)
# print the JSON string representation of the object
print(RenderEmailTemplateBody.to_json())

# convert the object into a dict
render_email_template_body_dict = render_email_template_body_instance.to_dict()
# create an instance of RenderEmailTemplateBody from a dict
render_email_template_body_from_dict = RenderEmailTemplateBody.from_dict(render_email_template_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


