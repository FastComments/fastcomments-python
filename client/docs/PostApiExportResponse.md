# PostApiExportResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**batch_job_id** | **str** |  | 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.post_api_export_response import PostApiExportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostApiExportResponse from a JSON string
post_api_export_response_instance = PostApiExportResponse.from_json(json)
# print the JSON string representation of the object
print(PostApiExportResponse.to_json())

# convert the object into a dict
post_api_export_response_dict = post_api_export_response_instance.to_dict()
# create an instance of PostApiExportResponse from a dict
post_api_export_response_from_dict = PostApiExportResponse.from_dict(post_api_export_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


