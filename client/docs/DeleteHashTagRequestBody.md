# DeleteHashTagRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | [optional] 

## Example

```python
from client.models.delete_hash_tag_request_body import DeleteHashTagRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteHashTagRequestBody from a JSON string
delete_hash_tag_request_body_instance = DeleteHashTagRequestBody.from_json(json)
# print the JSON string representation of the object
print(DeleteHashTagRequestBody.to_json())

# convert the object into a dict
delete_hash_tag_request_body_dict = delete_hash_tag_request_body_instance.to_dict()
# create an instance of DeleteHashTagRequestBody from a dict
delete_hash_tag_request_body_from_dict = DeleteHashTagRequestBody.from_dict(delete_hash_tag_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


