# CreateAPIPageData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessible_by_group_ids** | **List[str]** |  | [optional] 
**root_comment_count** | **int** |  | [optional] 
**comment_count** | **int** |  | [optional] 
**title** | **str** |  | 
**url** | **str** |  | 
**url_id** | **str** |  | 

## Example

```python
from generated.models.create_api_page_data import CreateAPIPageData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAPIPageData from a JSON string
create_api_page_data_instance = CreateAPIPageData.from_json(json)
# print the JSON string representation of the object
print(CreateAPIPageData.to_json())

# convert the object into a dict
create_api_page_data_dict = create_api_page_data_instance.to_dict()
# create an instance of CreateAPIPageData from a dict
create_api_page_data_from_dict = CreateAPIPageData.from_dict(create_api_page_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


