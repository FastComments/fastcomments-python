# PageUserEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_private** | **bool** |  | [optional] 
**avatar_src** | **str** |  | [optional] 
**display_name** | **str** |  | 
**id** | **str** |  | 

## Example

```python
from client.models.page_user_entry import PageUserEntry

# TODO update the JSON string below
json = "{}"
# create an instance of PageUserEntry from a JSON string
page_user_entry_instance = PageUserEntry.from_json(json)
# print the JSON string representation of the object
print(PageUserEntry.to_json())

# convert the object into a dict
page_user_entry_dict = page_user_entry_instance.to_dict()
# create an instance of PageUserEntry from a dict
page_user_entry_from_dict = PageUserEntry.from_dict(page_user_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


