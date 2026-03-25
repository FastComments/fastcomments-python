# ChangeTicketStateBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **int** |  | 

## Example

```python
from client.models.change_ticket_state_body import ChangeTicketStateBody

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeTicketStateBody from a JSON string
change_ticket_state_body_instance = ChangeTicketStateBody.from_json(json)
# print the JSON string representation of the object
print(ChangeTicketStateBody.to_json())

# convert the object into a dict
change_ticket_state_body_dict = change_ticket_state_body_instance.to_dict()
# create an instance of ChangeTicketStateBody from a dict
change_ticket_state_body_from_dict = ChangeTicketStateBody.from_dict(change_ticket_state_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


