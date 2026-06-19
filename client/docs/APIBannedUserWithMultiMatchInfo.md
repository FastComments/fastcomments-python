# APIBannedUserWithMultiMatchInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user_id** | **str** |  | [optional] 
**ban_type** | **str** |  | 
**email** | **str** |  | [optional] 
**ip_hash** | **str** |  | [optional] 
**banned_until** | **datetime** |  | 
**has_email_wildcard** | **bool** |  | 
**ban_reason** | **str** |  | [optional] 
**matches** | [**List[BannedUserMatch]**](BannedUserMatch.md) |  | 

## Example

```python
from client.models.api_banned_user_with_multi_match_info import APIBannedUserWithMultiMatchInfo

# TODO update the JSON string below
json = "{}"
# create an instance of APIBannedUserWithMultiMatchInfo from a JSON string
api_banned_user_with_multi_match_info_instance = APIBannedUserWithMultiMatchInfo.from_json(json)
# print the JSON string representation of the object
print(APIBannedUserWithMultiMatchInfo.to_json())

# convert the object into a dict
api_banned_user_with_multi_match_info_dict = api_banned_user_with_multi_match_info_instance.to_dict()
# create an instance of APIBannedUserWithMultiMatchInfo from a dict
api_banned_user_with_multi_match_info_from_dict = APIBannedUserWithMultiMatchInfo.from_dict(api_banned_user_with_multi_match_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


