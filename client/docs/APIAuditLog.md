# APIAuditLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user_id** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**resource_name** | **str** |  | 
**crud_type** | **str** |  | 
**var_from** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**ip** | **str** |  | [optional] 
**when** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**server_start_date** | **datetime** |  | [optional] 
**object_details** | **Dict[str, object]** | Construct a type with a set of properties K of type T | [optional] 

## Example

```python
from client.models.api_audit_log import APIAuditLog

# TODO update the JSON string below
json = "{}"
# create an instance of APIAuditLog from a JSON string
api_audit_log_instance = APIAuditLog.from_json(json)
# print the JSON string representation of the object
print(APIAuditLog.to_json())

# convert the object into a dict
api_audit_log_dict = api_audit_log_instance.to_dict()
# create an instance of APIAuditLog from a dict
api_audit_log_from_dict = APIAuditLog.from_dict(api_audit_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


