# GetEmailTemplateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**email_template** | [**CustomEmailTemplate**](CustomEmailTemplate.md) |  | 

## Example

```python
from client.models.get_email_template_response import GetEmailTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetEmailTemplateResponse from a JSON string
get_email_template_response_instance = GetEmailTemplateResponse.from_json(json)
# print the JSON string representation of the object
print(GetEmailTemplateResponse.to_json())

# convert the object into a dict
get_email_template_response_dict = get_email_template_response_instance.to_dict()
# create an instance of GetEmailTemplateResponse from a dict
get_email_template_response_from_dict = GetEmailTemplateResponse.from_dict(get_email_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


