# ModerationExportStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**job_status** | **str** |  | 
**record_count** | **int** |  | 
**download_url** | **str** |  | [optional] 

## Example

```python
from client.models.moderation_export_status_response import ModerationExportStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModerationExportStatusResponse from a JSON string
moderation_export_status_response_instance = ModerationExportStatusResponse.from_json(json)
# print the JSON string representation of the object
print(ModerationExportStatusResponse.to_json())

# convert the object into a dict
moderation_export_status_response_dict = moderation_export_status_response_instance.to_dict()
# create an instance of ModerationExportStatusResponse from a dict
moderation_export_status_response_from_dict = ModerationExportStatusResponse.from_dict(moderation_export_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


