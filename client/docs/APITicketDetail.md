# APITicketDetail


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
**files** | [**List[APITicketFile]**](APITicketFile.md) |  | 
**reopened_at** | **str** |  | [optional] 
**resolved_at** | **str** |  | [optional] 
**ack_at** | **str** |  | [optional] 

## Example

```python
from client.models.api_ticket_detail import APITicketDetail

# TODO update the JSON string below
json = "{}"
# create an instance of APITicketDetail from a JSON string
api_ticket_detail_instance = APITicketDetail.from_json(json)
# print the JSON string representation of the object
print(APITicketDetail.to_json())

# convert the object into a dict
api_ticket_detail_dict = api_ticket_detail_instance.to_dict()
# create an instance of APITicketDetail from a dict
api_ticket_detail_from_dict = APITicketDetail.from_dict(api_ticket_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


