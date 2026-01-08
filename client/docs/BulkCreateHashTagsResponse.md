# BulkCreateHashTagsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**results** | [**List[AddHashTag200Response]**](AddHashTag200Response.md) |  | 

## Example

```python
from client.models.bulk_create_hash_tags_response import BulkCreateHashTagsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkCreateHashTagsResponse from a JSON string
bulk_create_hash_tags_response_instance = BulkCreateHashTagsResponse.from_json(json)
# print the JSON string representation of the object
print(BulkCreateHashTagsResponse.to_json())

# convert the object into a dict
bulk_create_hash_tags_response_dict = bulk_create_hash_tags_response_instance.to_dict()
# create an instance of BulkCreateHashTagsResponse from a dict
bulk_create_hash_tags_response_from_dict = BulkCreateHashTagsResponse.from_dict(bulk_create_hash_tags_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


