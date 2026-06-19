# PreBanSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**usernames** | **List[str]** |  | 
**count** | **float** |  | 

## Example

```python
from client.models.pre_ban_summary import PreBanSummary

# TODO update the JSON string below
json = "{}"
# create an instance of PreBanSummary from a JSON string
pre_ban_summary_instance = PreBanSummary.from_json(json)
# print the JSON string representation of the object
print(PreBanSummary.to_json())

# convert the object into a dict
pre_ban_summary_dict = pre_ban_summary_instance.to_dict()
# create an instance of PreBanSummary from a dict
pre_ban_summary_from_dict = PreBanSummary.from_dict(pre_ban_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


