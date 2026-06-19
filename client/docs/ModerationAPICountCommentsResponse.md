# ModerationAPICountCommentsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**count** | **float** |  | 

## Example

```python
from client.models.moderation_api_count_comments_response import ModerationAPICountCommentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModerationAPICountCommentsResponse from a JSON string
moderation_api_count_comments_response_instance = ModerationAPICountCommentsResponse.from_json(json)
# print the JSON string representation of the object
print(ModerationAPICountCommentsResponse.to_json())

# convert the object into a dict
moderation_api_count_comments_response_dict = moderation_api_count_comments_response_instance.to_dict()
# create an instance of ModerationAPICountCommentsResponse from a dict
moderation_api_count_comments_response_from_dict = ModerationAPICountCommentsResponse.from_dict(moderation_api_count_comments_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


