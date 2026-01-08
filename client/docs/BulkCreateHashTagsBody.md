# BulkCreateHashTagsBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | [optional] 
**tags** | [**List[BulkCreateHashTagsBodyTagsInner]**](BulkCreateHashTagsBodyTagsInner.md) |  | 

## Example

```python
from client.models.bulk_create_hash_tags_body import BulkCreateHashTagsBody

# TODO update the JSON string below
json = "{}"
# create an instance of BulkCreateHashTagsBody from a JSON string
bulk_create_hash_tags_body_instance = BulkCreateHashTagsBody.from_json(json)
# print the JSON string representation of the object
print(BulkCreateHashTagsBody.to_json())

# convert the object into a dict
bulk_create_hash_tags_body_dict = bulk_create_hash_tags_body_instance.to_dict()
# create an instance of BulkCreateHashTagsBody from a dict
bulk_create_hash_tags_body_from_dict = BulkCreateHashTagsBody.from_dict(bulk_create_hash_tags_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


