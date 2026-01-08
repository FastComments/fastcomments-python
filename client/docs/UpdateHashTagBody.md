# UpdateHashTagBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**tag** | **str** |  | [optional] 

## Example

```python
from client.models.update_hash_tag_body import UpdateHashTagBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateHashTagBody from a JSON string
update_hash_tag_body_instance = UpdateHashTagBody.from_json(json)
# print the JSON string representation of the object
print(UpdateHashTagBody.to_json())

# convert the object into a dict
update_hash_tag_body_dict = update_hash_tag_body_instance.to_dict()
# create an instance of UpdateHashTagBody from a dict
update_hash_tag_body_from_dict = UpdateHashTagBody.from_dict(update_hash_tag_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


