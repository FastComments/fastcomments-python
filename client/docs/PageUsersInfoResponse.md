# PageUsersInfoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[PageUserEntry]**](PageUserEntry.md) |  | 
**status** | [**APIStatus**](APIStatus.md) |  | 

## Example

```python
from client.models.page_users_info_response import PageUsersInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PageUsersInfoResponse from a JSON string
page_users_info_response_instance = PageUsersInfoResponse.from_json(json)
# print the JSON string representation of the object
print(PageUsersInfoResponse.to_json())

# convert the object into a dict
page_users_info_response_dict = page_users_info_response_instance.to_dict()
# create an instance of PageUsersInfoResponse from a dict
page_users_info_response_from_dict = PageUsersInfoResponse.from_dict(page_users_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


