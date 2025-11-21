# APICreateUserBadgeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**user_badge** | [**UserBadge**](UserBadge.md) |  | 
**notes** | **List[str]** |  | [optional] 

## Example

```python
from client.models.api_create_user_badge_response import APICreateUserBadgeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of APICreateUserBadgeResponse from a JSON string
api_create_user_badge_response_instance = APICreateUserBadgeResponse.from_json(json)
# print the JSON string representation of the object
print(APICreateUserBadgeResponse.to_json())

# convert the object into a dict
api_create_user_badge_response_dict = api_create_user_badge_response_instance.to_dict()
# create an instance of APICreateUserBadgeResponse from a dict
api_create_user_badge_response_from_dict = APICreateUserBadgeResponse.from_dict(api_create_user_badge_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


