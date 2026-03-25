# CreateTicketResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**ticket** | [**APITicket**](APITicket.md) |  | 

## Example

```python
from client.models.create_ticket_response import CreateTicketResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTicketResponse from a JSON string
create_ticket_response_instance = CreateTicketResponse.from_json(json)
# print the JSON string representation of the object
print(CreateTicketResponse.to_json())

# convert the object into a dict
create_ticket_response_dict = create_ticket_response_instance.to_dict()
# create an instance of CreateTicketResponse from a dict
create_ticket_response_from_dict = CreateTicketResponse.from_dict(create_ticket_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


