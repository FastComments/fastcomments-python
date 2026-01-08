# EmailTemplateRenderErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**custom_template_id** | **str** |  | 
**error** | **str** |  | 
**count** | **float** |  | 
**created_at** | **datetime** |  | 
**last_occurred_at** | **datetime** |  | 

## Example

```python
from client.models.email_template_render_error_response import EmailTemplateRenderErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmailTemplateRenderErrorResponse from a JSON string
email_template_render_error_response_instance = EmailTemplateRenderErrorResponse.from_json(json)
# print the JSON string representation of the object
print(EmailTemplateRenderErrorResponse.to_json())

# convert the object into a dict
email_template_render_error_response_dict = email_template_render_error_response_instance.to_dict()
# create an instance of EmailTemplateRenderErrorResponse from a dict
email_template_render_error_response_from_dict = EmailTemplateRenderErrorResponse.from_dict(email_template_render_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


