# GetApiExportStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**job_status** | **str** |  | 
**record_count** | **int** |  | 
**download_url** | **str** |  | [optional] 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.get_api_export_status_response import GetApiExportStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetApiExportStatusResponse from a JSON string
get_api_export_status_response_instance = GetApiExportStatusResponse.from_json(json)
# print the JSON string representation of the object
print(GetApiExportStatusResponse.to_json())

# convert the object into a dict
get_api_export_status_response_dict = get_api_export_status_response_instance.to_dict()
# create an instance of GetApiExportStatusResponse from a dict
get_api_export_status_response_from_dict = GetApiExportStatusResponse.from_dict(get_api_export_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


