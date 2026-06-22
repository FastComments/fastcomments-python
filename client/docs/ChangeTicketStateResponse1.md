# ChangeTicketStateResponse1


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
from client.models.change_ticket_state_response1 import ChangeTicketStateResponse1

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeTicketStateResponse1 from a JSON string
change_ticket_state_response1_instance = ChangeTicketStateResponse1.from_json(json)
# print the JSON string representation of the object
print(ChangeTicketStateResponse1.to_json())

# convert the object into a dict
change_ticket_state_response1_dict = change_ticket_state_response1_instance.to_dict()
# create an instance of ChangeTicketStateResponse1 from a dict
change_ticket_state_response1_from_dict = ChangeTicketStateResponse1.from_dict(change_ticket_state_response1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


