# PickTenantAuditLogTenantAuditLogKeys

From T, pick a set of properties whose keys are in the union K

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**url** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**resource_name** | **str** |  | 
**crud_type** | **str** |  | 
**var_from** | **str** |  | [optional] 
**ip** | **str** |  | [optional] 
**when** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**server_start_date** | **datetime** |  | [optional] 
**object_details** | **Dict[str, object]** | Construct a type with a set of properties K of type T | [optional] 

## Example

```python
from client.models.pick_tenant_audit_log_tenant_audit_log_keys import PickTenantAuditLogTenantAuditLogKeys

# TODO update the JSON string below
json = "{}"
# create an instance of PickTenantAuditLogTenantAuditLogKeys from a JSON string
pick_tenant_audit_log_tenant_audit_log_keys_instance = PickTenantAuditLogTenantAuditLogKeys.from_json(json)
# print the JSON string representation of the object
print(PickTenantAuditLogTenantAuditLogKeys.to_json())

# convert the object into a dict
pick_tenant_audit_log_tenant_audit_log_keys_dict = pick_tenant_audit_log_tenant_audit_log_keys_instance.to_dict()
# create an instance of PickTenantAuditLogTenantAuditLogKeys from a dict
pick_tenant_audit_log_tenant_audit_log_keys_from_dict = PickTenantAuditLogTenantAuditLogKeys.from_dict(pick_tenant_audit_log_tenant_audit_log_keys_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


