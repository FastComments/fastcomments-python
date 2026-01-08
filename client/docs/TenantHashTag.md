# TenantHashTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**created_at** | **datetime** |  | 
**tenant_id** | **str** |  | 
**tag** | **str** |  | 
**url** | **str** |  | [optional] 

## Example

```python
from client.models.tenant_hash_tag import TenantHashTag

# TODO update the JSON string below
json = "{}"
# create an instance of TenantHashTag from a JSON string
tenant_hash_tag_instance = TenantHashTag.from_json(json)
# print the JSON string representation of the object
print(TenantHashTag.to_json())

# convert the object into a dict
tenant_hash_tag_dict = tenant_hash_tag_instance.to_dict()
# create an instance of TenantHashTag from a dict
tenant_hash_tag_from_dict = TenantHashTag.from_dict(tenant_hash_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


