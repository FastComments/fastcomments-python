# APIGetUserBadgeProgressResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**user_badge_progress** | [**UserBadgeProgress**](UserBadgeProgress.md) |  | 

## Example

```python
from client.models.api_get_user_badge_progress_response import APIGetUserBadgeProgressResponse

# TODO update the JSON string below
json = "{}"
# create an instance of APIGetUserBadgeProgressResponse from a JSON string
api_get_user_badge_progress_response_instance = APIGetUserBadgeProgressResponse.from_json(json)
# print the JSON string representation of the object
print(APIGetUserBadgeProgressResponse.to_json())

# convert the object into a dict
api_get_user_badge_progress_response_dict = api_get_user_badge_progress_response_instance.to_dict()
# create an instance of APIGetUserBadgeProgressResponse from a dict
api_get_user_badge_progress_response_from_dict = APIGetUserBadgeProgressResponse.from_dict(api_get_user_badge_progress_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


