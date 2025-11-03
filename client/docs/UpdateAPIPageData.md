# UpdateAPIPageData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_closed** | **bool** |  | [optional] 
**accessible_by_group_ids** | **List[str]** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**url_id** | **str** |  | [optional] 

## Example

```python
from client.models.update_api_page_data import UpdateAPIPageData

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAPIPageData from a JSON string
update_api_page_data_instance = UpdateAPIPageData.from_json(json)
# print the JSON string representation of the object
print(UpdateAPIPageData.to_json())

# convert the object into a dict
update_api_page_data_dict = update_api_page_data_instance.to_dict()
# create an instance of UpdateAPIPageData from a dict
update_api_page_data_from_dict = UpdateAPIPageData.from_dict(update_api_page_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


