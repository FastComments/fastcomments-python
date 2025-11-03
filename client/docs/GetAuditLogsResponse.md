# GetAuditLogsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**audit_logs** | [**List[PickTenantAuditLogTenantAuditLogKeys]**](PickTenantAuditLogTenantAuditLogKeys.md) |  | 

## Example

```python
from client.models.get_audit_logs_response import GetAuditLogsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAuditLogsResponse from a JSON string
get_audit_logs_response_instance = GetAuditLogsResponse.from_json(json)
# print the JSON string representation of the object
print(GetAuditLogsResponse.to_json())

# convert the object into a dict
get_audit_logs_response_dict = get_audit_logs_response_instance.to_dict()
# create an instance of GetAuditLogsResponse from a dict
get_audit_logs_response_from_dict = GetAuditLogsResponse.from_dict(get_audit_logs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


