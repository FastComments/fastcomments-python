# UnblockSuccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ImportedAPIStatusSUCCESS**](ImportedAPIStatusSUCCESS.md) |  | 
**comment_statuses** | **Dict[str, bool]** | Construct a type with a set of properties K of type T | 

## Example

```python
from generated.models.unblock_success import UnblockSuccess

# TODO update the JSON string below
json = "{}"
# create an instance of UnblockSuccess from a JSON string
unblock_success_instance = UnblockSuccess.from_json(json)
# print the JSON string representation of the object
print(UnblockSuccess.to_json())

# convert the object into a dict
unblock_success_dict = unblock_success_instance.to_dict()
# create an instance of UnblockSuccess from a dict
unblock_success_from_dict = UnblockSuccess.from_dict(unblock_success_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


