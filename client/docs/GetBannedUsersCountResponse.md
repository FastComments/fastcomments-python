# GetBannedUsersCountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **float** |  | 
**status** | **str** |  | 

## Example

```python
from client.models.get_banned_users_count_response import GetBannedUsersCountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetBannedUsersCountResponse from a JSON string
get_banned_users_count_response_instance = GetBannedUsersCountResponse.from_json(json)
# print the JSON string representation of the object
print(GetBannedUsersCountResponse.to_json())

# convert the object into a dict
get_banned_users_count_response_dict = get_banned_users_count_response_instance.to_dict()
# create an instance of GetBannedUsersCountResponse from a dict
get_banned_users_count_response_from_dict = GetBannedUsersCountResponse.from_dict(get_banned_users_count_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


