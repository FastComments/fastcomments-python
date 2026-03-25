# APITicket


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**url_id** | **str** |  | 
**user_id** | **str** |  | 
**managed_by_tenant_id** | **str** |  | 
**assigned_user_ids** | **List[str]** |  | 
**subject** | **str** |  | 
**created_at** | **str** |  | 
**state** | **int** |  | 
**file_count** | **int** |  | 

## Example

```python
from client.models.api_ticket import APITicket

# TODO update the JSON string below
json = "{}"
# create an instance of APITicket from a JSON string
api_ticket_instance = APITicket.from_json(json)
# print the JSON string representation of the object
print(APITicket.to_json())

# convert the object into a dict
api_ticket_dict = api_ticket_instance.to_dict()
# create an instance of APITicket from a dict
api_ticket_from_dict = APITicket.from_dict(api_ticket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


