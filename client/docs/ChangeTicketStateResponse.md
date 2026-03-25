# ChangeTicketStateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**ticket** | [**APITicket**](APITicket.md) |  | 

## Example

```python
from client.models.change_ticket_state_response import ChangeTicketStateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeTicketStateResponse from a JSON string
change_ticket_state_response_instance = ChangeTicketStateResponse.from_json(json)
# print the JSON string representation of the object
print(ChangeTicketStateResponse.to_json())

# convert the object into a dict
change_ticket_state_response_dict = change_ticket_state_response_instance.to_dict()
# create an instance of ChangeTicketStateResponse from a dict
change_ticket_state_response_from_dict = ChangeTicketStateResponse.from_dict(change_ticket_state_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


