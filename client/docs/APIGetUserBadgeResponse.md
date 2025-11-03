# APIGetUserBadgeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**user_badge** | [**UserBadge**](UserBadge.md) |  | 

## Example

```python
from generated.models.api_get_user_badge_response import APIGetUserBadgeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of APIGetUserBadgeResponse from a JSON string
api_get_user_badge_response_instance = APIGetUserBadgeResponse.from_json(json)
# print the JSON string representation of the object
print(APIGetUserBadgeResponse.to_json())

# convert the object into a dict
api_get_user_badge_response_dict = api_get_user_badge_response_instance.to_dict()
# create an instance of APIGetUserBadgeResponse from a dict
api_get_user_badge_response_from_dict = APIGetUserBadgeResponse.from_dict(api_get_user_badge_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


