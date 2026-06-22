# PostBulkPreBanSummaryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**total_related_comment_count** | **int** |  | 
**email_domains** | **List[str]** |  | 
**emails** | **List[str]** |  | 
**user_ids** | **List[str]** |  | 
**ip_hashes** | **List[str]** |  | 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.post_bulk_pre_ban_summary_response import PostBulkPreBanSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostBulkPreBanSummaryResponse from a JSON string
post_bulk_pre_ban_summary_response_instance = PostBulkPreBanSummaryResponse.from_json(json)
# print the JSON string representation of the object
print(PostBulkPreBanSummaryResponse.to_json())

# convert the object into a dict
post_bulk_pre_ban_summary_response_dict = post_bulk_pre_ban_summary_response_instance.to_dict()
# create an instance of PostBulkPreBanSummaryResponse from a dict
post_bulk_pre_ban_summary_response_from_dict = PostBulkPreBanSummaryResponse.from_dict(post_bulk_pre_ban_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


