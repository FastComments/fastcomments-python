# GetUserManualBadgesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**badges** | [**List[UserBadge]**](UserBadge.md) |  | 
**status** | [**APIStatus**](APIStatus.md) |  | 

## Example

```python
from client.models.get_user_manual_badges_response import GetUserManualBadgesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserManualBadgesResponse from a JSON string
get_user_manual_badges_response_instance = GetUserManualBadgesResponse.from_json(json)
# print the JSON string representation of the object
print(GetUserManualBadgesResponse.to_json())

# convert the object into a dict
get_user_manual_badges_response_dict = get_user_manual_badges_response_instance.to_dict()
# create an instance of GetUserManualBadgesResponse from a dict
get_user_manual_badges_response_from_dict = GetUserManualBadgesResponse.from_dict(get_user_manual_badges_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


