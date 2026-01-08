# CreateHashTagBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | [optional] 
**tag** | **str** |  | 
**url** | **str** |  | [optional] 

## Example

```python
from client.models.create_hash_tag_body import CreateHashTagBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreateHashTagBody from a JSON string
create_hash_tag_body_instance = CreateHashTagBody.from_json(json)
# print the JSON string representation of the object
print(CreateHashTagBody.to_json())

# convert the object into a dict
create_hash_tag_body_dict = create_hash_tag_body_instance.to_dict()
# create an instance of CreateHashTagBody from a dict
create_hash_tag_body_from_dict = CreateHashTagBody.from_dict(create_hash_tag_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


