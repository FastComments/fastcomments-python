# ModerationExportResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**batch_job_id** | **str** |  | 

## Example

```python
from client.models.moderation_export_response import ModerationExportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModerationExportResponse from a JSON string
moderation_export_response_instance = ModerationExportResponse.from_json(json)
# print the JSON string representation of the object
print(ModerationExportResponse.to_json())

# convert the object into a dict
moderation_export_response_dict = moderation_export_response_instance.to_dict()
# create an instance of ModerationExportResponse from a dict
moderation_export_response_from_dict = ModerationExportResponse.from_dict(moderation_export_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


