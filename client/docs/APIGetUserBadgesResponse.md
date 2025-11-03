# APIGetUserBadgesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**user_badges** | [**List[UserBadge]**](UserBadge.md) |  | 

## Example

```python
from client.models.api_get_user_badges_response import APIGetUserBadgesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of APIGetUserBadgesResponse from a JSON string
api_get_user_badges_response_instance = APIGetUserBadgesResponse.from_json(json)
# print the JSON string representation of the object
print(APIGetUserBadgesResponse.to_json())

# convert the object into a dict
api_get_user_badges_response_dict = api_get_user_badges_response_instance.to_dict()
# create an instance of APIGetUserBadgesResponse from a dict
api_get_user_badges_response_from_dict = APIGetUserBadgesResponse.from_dict(api_get_user_badges_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


