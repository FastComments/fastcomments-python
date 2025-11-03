# MetaItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**values** | **List[str]** |  | 

## Example

```python
from client.models.meta_item import MetaItem

# TODO update the JSON string below
json = "{}"
# create an instance of MetaItem from a JSON string
meta_item_instance = MetaItem.from_json(json)
# print the JSON string representation of the object
print(MetaItem.to_json())

# convert the object into a dict
meta_item_dict = meta_item_instance.to_dict()
# create an instance of MetaItem from a dict
meta_item_from_dict = MetaItem.from_dict(meta_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


