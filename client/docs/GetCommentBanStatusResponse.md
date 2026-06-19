# GetCommentBanStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**email_domain** | **str** |  | 
**can_ip_ban** | **bool** |  | 

## Example

```python
from client.models.get_comment_ban_status_response import GetCommentBanStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCommentBanStatusResponse from a JSON string
get_comment_ban_status_response_instance = GetCommentBanStatusResponse.from_json(json)
# print the JSON string representation of the object
print(GetCommentBanStatusResponse.to_json())

# convert the object into a dict
get_comment_ban_status_response_dict = get_comment_ban_status_response_instance.to_dict()
# create an instance of GetCommentBanStatusResponse from a dict
get_comment_ban_status_response_from_dict = GetCommentBanStatusResponse.from_dict(get_comment_ban_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


