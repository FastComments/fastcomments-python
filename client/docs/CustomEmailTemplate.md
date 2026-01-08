# CustomEmailTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**email_template_id** | **str** |  | 
**display_name** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**updated_by_user_id** | **str** |  | 
**domain** | **str** |  | [optional] 
**ejs** | **str** |  | 
**translation_overrides_by_locale** | **Dict[str, Dict[str, str]]** | Construct a type with a set of properties K of type T | 
**test_data** | **object** |  | 

## Example

```python
from client.models.custom_email_template import CustomEmailTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of CustomEmailTemplate from a JSON string
custom_email_template_instance = CustomEmailTemplate.from_json(json)
# print the JSON string representation of the object
print(CustomEmailTemplate.to_json())

# convert the object into a dict
custom_email_template_dict = custom_email_template_instance.to_dict()
# create an instance of CustomEmailTemplate from a dict
custom_email_template_from_dict = CustomEmailTemplate.from_dict(custom_email_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


