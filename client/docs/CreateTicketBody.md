# CreateTicketBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | **str** |  | 

## Example

```python
from client.models.create_ticket_body import CreateTicketBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTicketBody from a JSON string
create_ticket_body_instance = CreateTicketBody.from_json(json)
# print the JSON string representation of the object
print(CreateTicketBody.to_json())

# convert the object into a dict
create_ticket_body_dict = create_ticket_body_instance.to_dict()
# create an instance of CreateTicketBody from a dict
create_ticket_body_from_dict = CreateTicketBody.from_dict(create_ticket_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


