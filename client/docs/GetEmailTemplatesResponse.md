# GetEmailTemplatesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**email_templates** | [**List[CustomEmailTemplate]**](CustomEmailTemplate.md) |  | 

## Example

```python
from client.models.get_email_templates_response import GetEmailTemplatesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetEmailTemplatesResponse from a JSON string
get_email_templates_response_instance = GetEmailTemplatesResponse.from_json(json)
# print the JSON string representation of the object
print(GetEmailTemplatesResponse.to_json())

# convert the object into a dict
get_email_templates_response_dict = get_email_templates_response_instance.to_dict()
# create an instance of GetEmailTemplatesResponse from a dict
get_email_templates_response_from_dict = GetEmailTemplatesResponse.from_dict(get_email_templates_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


