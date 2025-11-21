# CheckBlockedCommentsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment_statuses** | **Dict[str, bool]** | Construct a type with a set of properties K of type T | 
**status** | [**APIStatus**](APIStatus.md) |  | 

## Example

```python
from client.models.check_blocked_comments_response import CheckBlockedCommentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CheckBlockedCommentsResponse from a JSON string
check_blocked_comments_response_instance = CheckBlockedCommentsResponse.from_json(json)
# print the JSON string representation of the object
print(CheckBlockedCommentsResponse.to_json())

# convert the object into a dict
check_blocked_comments_response_dict = check_blocked_comments_response_instance.to_dict()
# create an instance of CheckBlockedCommentsResponse from a dict
check_blocked_comments_response_from_dict = CheckBlockedCommentsResponse.from_dict(check_blocked_comments_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


