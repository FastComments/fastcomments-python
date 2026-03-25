# CreateTicket200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**ticket** | [**APITicket**](APITicket.md) |  | 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.create_ticket200_response import CreateTicket200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTicket200Response from a JSON string
create_ticket200_response_instance = CreateTicket200Response.from_json(json)
# print the JSON string representation of the object
print(CreateTicket200Response.to_json())

# convert the object into a dict
create_ticket200_response_dict = create_ticket200_response_instance.to_dict()
# create an instance of CreateTicket200Response from a dict
create_ticket200_response_from_dict = CreateTicket200Response.from_dict(create_ticket200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


