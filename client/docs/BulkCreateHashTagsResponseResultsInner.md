# BulkCreateHashTagsResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**hash_tag** | [**TenantHashTag**](TenantHashTag.md) |  | 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.bulk_create_hash_tags_response_results_inner import BulkCreateHashTagsResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BulkCreateHashTagsResponseResultsInner from a JSON string
bulk_create_hash_tags_response_results_inner_instance = BulkCreateHashTagsResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(BulkCreateHashTagsResponseResultsInner.to_json())

# convert the object into a dict
bulk_create_hash_tags_response_results_inner_dict = bulk_create_hash_tags_response_results_inner_instance.to_dict()
# create an instance of BulkCreateHashTagsResponseResultsInner from a dict
bulk_create_hash_tags_response_results_inner_from_dict = BulkCreateHashTagsResponseResultsInner.from_dict(bulk_create_hash_tags_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


