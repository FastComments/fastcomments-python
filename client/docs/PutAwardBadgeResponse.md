# PutAwardBadgeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notes** | **List[str]** |  | [optional] 
**badges** | [**List[CommentUserBadgeInfo]**](CommentUserBadgeInfo.md) |  | [optional] 
**status** | [**APIStatus**](APIStatus.md) |  | 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.put_award_badge_response import PutAwardBadgeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutAwardBadgeResponse from a JSON string
put_award_badge_response_instance = PutAwardBadgeResponse.from_json(json)
# print the JSON string representation of the object
print(PutAwardBadgeResponse.to_json())

# convert the object into a dict
put_award_badge_response_dict = put_award_badge_response_instance.to_dict()
# create an instance of PutAwardBadgeResponse from a dict
put_award_badge_response_from_dict = PutAwardBadgeResponse.from_dict(put_award_badge_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


