# SetCommentApprovedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**did_reset_flagged_count** | **bool** |  | [optional] 
**status** | [**APIStatus**](APIStatus.md) |  | 

## Example

```python
from client.models.set_comment_approved_response import SetCommentApprovedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SetCommentApprovedResponse from a JSON string
set_comment_approved_response_instance = SetCommentApprovedResponse.from_json(json)
# print the JSON string representation of the object
print(SetCommentApprovedResponse.to_json())

# convert the object into a dict
set_comment_approved_response_dict = set_comment_approved_response_instance.to_dict()
# create an instance of SetCommentApprovedResponse from a dict
set_comment_approved_response_from_dict = SetCommentApprovedResponse.from_dict(set_comment_approved_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


