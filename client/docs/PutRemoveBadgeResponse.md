# PutRemoveBadgeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
from client.models.put_remove_badge_response import PutRemoveBadgeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutRemoveBadgeResponse from a JSON string
put_remove_badge_response_instance = PutRemoveBadgeResponse.from_json(json)
# print the JSON string representation of the object
print(PutRemoveBadgeResponse.to_json())

# convert the object into a dict
put_remove_badge_response_dict = put_remove_badge_response_instance.to_dict()
# create an instance of PutRemoveBadgeResponse from a dict
put_remove_badge_response_from_dict = PutRemoveBadgeResponse.from_dict(put_remove_badge_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


