# BulkPreBanSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**total_related_comment_count** | **int** |  | 
**email_domains** | **List[str]** |  | 
**emails** | **List[str]** |  | 
**user_ids** | **List[str]** |  | 
**ip_hashes** | **List[str]** |  | 

## Example

```python
from client.models.bulk_pre_ban_summary import BulkPreBanSummary

# TODO update the JSON string below
json = "{}"
# create an instance of BulkPreBanSummary from a JSON string
bulk_pre_ban_summary_instance = BulkPreBanSummary.from_json(json)
# print the JSON string representation of the object
print(BulkPreBanSummary.to_json())

# convert the object into a dict
bulk_pre_ban_summary_dict = bulk_pre_ban_summary_instance.to_dict()
# create an instance of BulkPreBanSummary from a dict
bulk_pre_ban_summary_from_dict = BulkPreBanSummary.from_dict(bulk_pre_ban_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


