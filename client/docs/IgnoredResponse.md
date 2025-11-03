# IgnoredResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ImportedAPIStatusSUCCESS**](ImportedAPIStatusSUCCESS.md) |  | 
**note** | **str** |  | 

## Example

```python
from client.models.ignored_response import IgnoredResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IgnoredResponse from a JSON string
ignored_response_instance = IgnoredResponse.from_json(json)
# print the JSON string representation of the object
print(IgnoredResponse.to_json())

# convert the object into a dict
ignored_response_dict = ignored_response_instance.to_dict()
# create an instance of IgnoredResponse from a dict
ignored_response_from_dict = IgnoredResponse.from_dict(ignored_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


