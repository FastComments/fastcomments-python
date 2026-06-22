# GetPreBanSummaryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**usernames** | **List[str]** |  | 
**count** | **float** |  | 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.get_pre_ban_summary_response import GetPreBanSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetPreBanSummaryResponse from a JSON string
get_pre_ban_summary_response_instance = GetPreBanSummaryResponse.from_json(json)
# print the JSON string representation of the object
print(GetPreBanSummaryResponse.to_json())

# convert the object into a dict
get_pre_ban_summary_response_dict = get_pre_ban_summary_response_instance.to_dict()
# create an instance of GetPreBanSummaryResponse from a dict
get_pre_ban_summary_response_from_dict = GetPreBanSummaryResponse.from_dict(get_pre_ban_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


