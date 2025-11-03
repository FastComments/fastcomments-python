# APIGetUserBadgeProgressListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**user_badge_progresses** | [**List[UserBadgeProgress]**](UserBadgeProgress.md) |  | 

## Example

```python
from generated.models.api_get_user_badge_progress_list_response import APIGetUserBadgeProgressListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of APIGetUserBadgeProgressListResponse from a JSON string
api_get_user_badge_progress_list_response_instance = APIGetUserBadgeProgressListResponse.from_json(json)
# print the JSON string representation of the object
print(APIGetUserBadgeProgressListResponse.to_json())

# convert the object into a dict
api_get_user_badge_progress_list_response_dict = api_get_user_badge_progress_list_response_instance.to_dict()
# create an instance of APIGetUserBadgeProgressListResponse from a dict
api_get_user_badge_progress_list_response_from_dict = APIGetUserBadgeProgressListResponse.from_dict(api_get_user_badge_progress_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


