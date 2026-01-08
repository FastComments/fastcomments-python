# DeleteHashTagRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | [optional] 

## Example

```python
from client.models.delete_hash_tag_request import DeleteHashTagRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteHashTagRequest from a JSON string
delete_hash_tag_request_instance = DeleteHashTagRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteHashTagRequest.to_json())

# convert the object into a dict
delete_hash_tag_request_dict = delete_hash_tag_request_instance.to_dict()
# create an instance of DeleteHashTagRequest from a dict
delete_hash_tag_request_from_dict = DeleteHashTagRequest.from_dict(delete_hash_tag_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


