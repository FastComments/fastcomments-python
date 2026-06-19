# GetV2PageReacts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reacted_ids** | **List[str]** |  | [optional] 
**counts** | **Dict[str, float]** | Construct a type with a set of properties K of type T | [optional] 
**status** | [**APIStatus**](APIStatus.md) |  | 

## Example

```python
from client.models.get_v2_page_reacts import GetV2PageReacts

# TODO update the JSON string below
json = "{}"
# create an instance of GetV2PageReacts from a JSON string
get_v2_page_reacts_instance = GetV2PageReacts.from_json(json)
# print the JSON string representation of the object
print(GetV2PageReacts.to_json())

# convert the object into a dict
get_v2_page_reacts_dict = get_v2_page_reacts_instance.to_dict()
# create an instance of GetV2PageReacts from a dict
get_v2_page_reacts_from_dict = GetV2PageReacts.from_dict(get_v2_page_reacts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


