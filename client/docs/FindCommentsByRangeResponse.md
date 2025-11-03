# FindCommentsByRangeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[FindCommentsByRangeItem]**](FindCommentsByRangeItem.md) |  | 
**created_at** | **datetime** |  | 

## Example

```python
from client.models.find_comments_by_range_response import FindCommentsByRangeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FindCommentsByRangeResponse from a JSON string
find_comments_by_range_response_instance = FindCommentsByRangeResponse.from_json(json)
# print the JSON string representation of the object
print(FindCommentsByRangeResponse.to_json())

# convert the object into a dict
find_comments_by_range_response_dict = find_comments_by_range_response_instance.to_dict()
# create an instance of FindCommentsByRangeResponse from a dict
find_comments_by_range_response_from_dict = FindCommentsByRangeResponse.from_dict(find_comments_by_range_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


