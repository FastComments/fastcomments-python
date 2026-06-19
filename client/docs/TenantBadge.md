# TenantBadge


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**created_by_user_id** | **str** |  | 
**created_at** | **datetime** |  | 
**enabled** | **bool** |  | 
**url_id** | **str** |  | [optional] 
**type** | **float** |  | 
**threshold** | **float** |  | 
**uses** | **float** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**display_label** | **str** |  | 
**display_src** | **str** |  | 
**background_color** | **str** |  | 
**border_color** | **str** |  | 
**text_color** | **str** |  | 
**css_class** | **str** |  | [optional] 
**veteran_user_threshold_millis** | **float** |  | [optional] 
**is_awaiting_reprocess** | **bool** |  | 
**is_awaiting_deletion** | **bool** |  | 
**replaces_badge_id** | **str** |  | [optional] 

## Example

```python
from client.models.tenant_badge import TenantBadge

# TODO update the JSON string below
json = "{}"
# create an instance of TenantBadge from a JSON string
tenant_badge_instance = TenantBadge.from_json(json)
# print the JSON string representation of the object
print(TenantBadge.to_json())

# convert the object into a dict
tenant_badge_dict = tenant_badge_instance.to_dict()
# create an instance of TenantBadge from a dict
tenant_badge_from_dict = TenantBadge.from_dict(tenant_badge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


