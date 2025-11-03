# APIPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_closed** | **bool** |  | [optional] 
**accessible_by_group_ids** | **List[str]** |  | [optional] 
**root_comment_count** | **int** |  | 
**comment_count** | **int** |  | 
**created_at** | **datetime** |  | 
**title** | **str** |  | 
**url** | **str** |  | [optional] 
**url_id** | **str** |  | 
**id** | **str** |  | 

## Example

```python
from client.models.api_page import APIPage

# TODO update the JSON string below
json = "{}"
# create an instance of APIPage from a JSON string
api_page_instance = APIPage.from_json(json)
# print the JSON string representation of the object
print(APIPage.to_json())

# convert the object into a dict
api_page_dict = api_page_instance.to_dict()
# create an instance of APIPage from a dict
api_page_from_dict = APIPage.from_dict(api_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


