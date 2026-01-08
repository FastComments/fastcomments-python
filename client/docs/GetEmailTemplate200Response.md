# GetEmailTemplate200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**email_template** | [**CustomEmailTemplate**](CustomEmailTemplate.md) |  | 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.get_email_template200_response import GetEmailTemplate200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetEmailTemplate200Response from a JSON string
get_email_template200_response_instance = GetEmailTemplate200Response.from_json(json)
# print the JSON string representation of the object
print(GetEmailTemplate200Response.to_json())

# convert the object into a dict
get_email_template200_response_dict = get_email_template200_response_instance.to_dict()
# create an instance of GetEmailTemplate200Response from a dict
get_email_template200_response_from_dict = GetEmailTemplate200Response.from_dict(get_email_template200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


