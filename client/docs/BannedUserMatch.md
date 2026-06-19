# BannedUserMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**matched_on** | [**BannedUserMatchType**](BannedUserMatchType.md) |  | 
**matched_on_value** | [**BannedUserMatchMatchedOnValue**](BannedUserMatchMatchedOnValue.md) |  | 

## Example

```python
from client.models.banned_user_match import BannedUserMatch

# TODO update the JSON string below
json = "{}"
# create an instance of BannedUserMatch from a JSON string
banned_user_match_instance = BannedUserMatch.from_json(json)
# print the JSON string representation of the object
print(BannedUserMatch.to_json())

# convert the object into a dict
banned_user_match_dict = banned_user_match_instance.to_dict()
# create an instance of BannedUserMatch from a dict
banned_user_match_from_dict = BannedUserMatch.from_dict(banned_user_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


