# GetTicketResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**ticket** | [**APITicketDetail**](APITicketDetail.md) |  | 
**available_states** | **List[float]** |  | 

## Example

```python
from client.models.get_ticket_response import GetTicketResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTicketResponse from a JSON string
get_ticket_response_instance = GetTicketResponse.from_json(json)
# print the JSON string representation of the object
print(GetTicketResponse.to_json())

# convert the object into a dict
get_ticket_response_dict = get_ticket_response_instance.to_dict()
# create an instance of GetTicketResponse from a dict
get_ticket_response_from_dict = GetTicketResponse.from_dict(get_ticket_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


