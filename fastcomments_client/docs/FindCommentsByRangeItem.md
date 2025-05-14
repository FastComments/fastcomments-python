# FindCommentsByRangeItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | [**FComment**](FComment.md) |  | 
**result** | [**QuestionResult**](QuestionResult.md) |  | 

## Example

```python
from openapi_client.models.find_comments_by_range_item import FindCommentsByRangeItem

# TODO update the JSON string below
json = "{}"
# create an instance of FindCommentsByRangeItem from a JSON string
find_comments_by_range_item_instance = FindCommentsByRangeItem.from_json(json)
# print the JSON string representation of the object
print(FindCommentsByRangeItem.to_json())

# convert the object into a dict
find_comments_by_range_item_dict = find_comments_by_range_item_instance.to_dict()
# create an instance of FindCommentsByRangeItem from a dict
find_comments_by_range_item_from_dict = FindCommentsByRangeItem.from_dict(find_comments_by_range_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


