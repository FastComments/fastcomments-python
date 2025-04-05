# ChangeCommentPinStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment_positions** | [**Dict[str, RecordStringBeforeStringOrNullAfterStringOrNullValue]**](RecordStringBeforeStringOrNullAfterStringOrNullValue.md) | Construct a type with a set of properties K of type T | 
**status** | [**ImportedAPIStatusSUCCESS**](ImportedAPIStatusSUCCESS.md) |  | 

## Example

```python
from openapi_client.models.change_comment_pin_status_response import ChangeCommentPinStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeCommentPinStatusResponse from a JSON string
change_comment_pin_status_response_instance = ChangeCommentPinStatusResponse.from_json(json)
# print the JSON string representation of the object
print(ChangeCommentPinStatusResponse.to_json())

# convert the object into a dict
change_comment_pin_status_response_dict = change_comment_pin_status_response_instance.to_dict()
# create an instance of ChangeCommentPinStatusResponse from a dict
change_comment_pin_status_response_from_dict = ChangeCommentPinStatusResponse.from_dict(change_comment_pin_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


