# RenderEmailTemplateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**html** | **str** |  | 

## Example

```python
from client.models.render_email_template_response import RenderEmailTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RenderEmailTemplateResponse from a JSON string
render_email_template_response_instance = RenderEmailTemplateResponse.from_json(json)
# print the JSON string representation of the object
print(RenderEmailTemplateResponse.to_json())

# convert the object into a dict
render_email_template_response_dict = render_email_template_response_instance.to_dict()
# create an instance of RenderEmailTemplateResponse from a dict
render_email_template_response_from_dict = RenderEmailTemplateResponse.from_dict(render_email_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


