# RenderEmailTemplate200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**html** | **str** |  | 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.render_email_template200_response import RenderEmailTemplate200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RenderEmailTemplate200Response from a JSON string
render_email_template200_response_instance = RenderEmailTemplate200Response.from_json(json)
# print the JSON string representation of the object
print(RenderEmailTemplate200Response.to_json())

# convert the object into a dict
render_email_template200_response_dict = render_email_template200_response_instance.to_dict()
# create an instance of RenderEmailTemplate200Response from a dict
render_email_template200_response_from_dict = RenderEmailTemplate200Response.from_dict(render_email_template200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


