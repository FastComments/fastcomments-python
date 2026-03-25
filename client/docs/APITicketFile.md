# APITicketFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**s3_key** | **str** |  | 
**original_file_name** | **str** |  | 
**size_bytes** | **int** |  | 
**content_type** | **str** |  | 
**uploaded_by_user_id** | **str** |  | 
**uploaded_at** | **str** |  | 
**url** | **str** |  | 
**expires_at** | **str** |  | 
**expired** | **bool** |  | [optional] 

## Example

```python
from client.models.api_ticket_file import APITicketFile

# TODO update the JSON string below
json = "{}"
# create an instance of APITicketFile from a JSON string
api_ticket_file_instance = APITicketFile.from_json(json)
# print the JSON string representation of the object
print(APITicketFile.to_json())

# convert the object into a dict
api_ticket_file_dict = api_ticket_file_instance.to_dict()
# create an instance of APITicketFile from a dict
api_ticket_file_from_dict = APITicketFile.from_dict(api_ticket_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


