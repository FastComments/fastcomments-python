# PageUsersOfflineResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_after_user_id** | **str** |  | 
**next_after_name** | **str** |  | 
**users** | [**List[PageUserEntry]**](PageUserEntry.md) |  | 
**status** | [**APIStatus**](APIStatus.md) |  | 

## Example

```python
from client.models.page_users_offline_response import PageUsersOfflineResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PageUsersOfflineResponse from a JSON string
page_users_offline_response_instance = PageUsersOfflineResponse.from_json(json)
# print the JSON string representation of the object
print(PageUsersOfflineResponse.to_json())

# convert the object into a dict
page_users_offline_response_dict = page_users_offline_response_instance.to_dict()
# create an instance of PageUsersOfflineResponse from a dict
page_users_offline_response_from_dict = PageUsersOfflineResponse.from_dict(page_users_offline_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


