# ModerationAPIGetLogsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logs** | [**List[ModerationAPICommentLog]**](ModerationAPICommentLog.md) |  | 
**status** | [**APIStatus**](APIStatus.md) |  | 

## Example

```python
from client.models.moderation_api_get_logs_response import ModerationAPIGetLogsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModerationAPIGetLogsResponse from a JSON string
moderation_api_get_logs_response_instance = ModerationAPIGetLogsResponse.from_json(json)
# print the JSON string representation of the object
print(ModerationAPIGetLogsResponse.to_json())

# convert the object into a dict
moderation_api_get_logs_response_dict = moderation_api_get_logs_response_instance.to_dict()
# create an instance of ModerationAPIGetLogsResponse from a dict
moderation_api_get_logs_response_from_dict = ModerationAPIGetLogsResponse.from_dict(moderation_api_get_logs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


