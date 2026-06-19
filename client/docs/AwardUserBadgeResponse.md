# AwardUserBadgeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notes** | **List[str]** |  | [optional] 
**badges** | [**List[CommentUserBadgeInfo]**](CommentUserBadgeInfo.md) |  | [optional] 
**status** | [**APIStatus**](APIStatus.md) |  | 

## Example

```python
from client.models.award_user_badge_response import AwardUserBadgeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AwardUserBadgeResponse from a JSON string
award_user_badge_response_instance = AwardUserBadgeResponse.from_json(json)
# print the JSON string representation of the object
print(AwardUserBadgeResponse.to_json())

# convert the object into a dict
award_user_badge_response_dict = award_user_badge_response_instance.to_dict()
# create an instance of AwardUserBadgeResponse from a dict
award_user_badge_response_from_dict = AwardUserBadgeResponse.from_dict(award_user_badge_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


