# AddHashTagsBulkResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**results** | [**List[BulkCreateHashTagsResponseResultsInner]**](BulkCreateHashTagsResponseResultsInner.md) |  | 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.add_hash_tags_bulk_response import AddHashTagsBulkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddHashTagsBulkResponse from a JSON string
add_hash_tags_bulk_response_instance = AddHashTagsBulkResponse.from_json(json)
# print the JSON string representation of the object
print(AddHashTagsBulkResponse.to_json())

# convert the object into a dict
add_hash_tags_bulk_response_dict = add_hash_tags_bulk_response_instance.to_dict()
# create an instance of AddHashTagsBulkResponse from a dict
add_hash_tags_bulk_response_from_dict = AddHashTagsBulkResponse.from_dict(add_hash_tags_bulk_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


