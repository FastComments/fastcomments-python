# GetEmailTemplateRenderErrorsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**render_errors** | [**List[EmailTemplateRenderErrorResponse]**](EmailTemplateRenderErrorResponse.md) |  | 

## Example

```python
from client.models.get_email_template_render_errors_response import GetEmailTemplateRenderErrorsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetEmailTemplateRenderErrorsResponse from a JSON string
get_email_template_render_errors_response_instance = GetEmailTemplateRenderErrorsResponse.from_json(json)
# print the JSON string representation of the object
print(GetEmailTemplateRenderErrorsResponse.to_json())

# convert the object into a dict
get_email_template_render_errors_response_dict = get_email_template_render_errors_response_instance.to_dict()
# create an instance of GetEmailTemplateRenderErrorsResponse from a dict
get_email_template_render_errors_response_from_dict = GetEmailTemplateRenderErrorsResponse.from_dict(get_email_template_render_errors_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


