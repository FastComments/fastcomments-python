# GetTenantManualBadgesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**badges** | [**List[TenantBadge]**](TenantBadge.md) |  | 
**status** | [**APIStatus**](APIStatus.md) |  | 

## Example

```python
from client.models.get_tenant_manual_badges_response import GetTenantManualBadgesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTenantManualBadgesResponse from a JSON string
get_tenant_manual_badges_response_instance = GetTenantManualBadgesResponse.from_json(json)
# print the JSON string representation of the object
print(GetTenantManualBadgesResponse.to_json())

# convert the object into a dict
get_tenant_manual_badges_response_dict = get_tenant_manual_badges_response_instance.to_dict()
# create an instance of GetTenantManualBadgesResponse from a dict
get_tenant_manual_badges_response_from_dict = GetTenantManualBadgesResponse.from_dict(get_tenant_manual_badges_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


