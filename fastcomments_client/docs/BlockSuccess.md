# BlockSuccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ImportedAPIStatusSUCCESS**](ImportedAPIStatusSUCCESS.md) |  | 
**comment_statuses** | **Dict[str, bool]** | Construct a type with a set of properties K of type T | 

## Example

```python
from openapi_client.models.block_success import BlockSuccess

# TODO update the JSON string below
json = "{}"
# create an instance of BlockSuccess from a JSON string
block_success_instance = BlockSuccess.from_json(json)
# print the JSON string representation of the object
print(BlockSuccess.to_json())

# convert the object into a dict
block_success_dict = block_success_instance.to_dict()
# create an instance of BlockSuccess from a dict
block_success_from_dict = BlockSuccess.from_dict(block_success_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


