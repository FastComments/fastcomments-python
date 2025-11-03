# APIGetCommentsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**comments** | [**List[PickFCommentAPICommentFieldsKeys]**](PickFCommentAPICommentFieldsKeys.md) |  | 

## Example

```python
from generated.models.api_get_comments_response import APIGetCommentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of APIGetCommentsResponse from a JSON string
api_get_comments_response_instance = APIGetCommentsResponse.from_json(json)
# print the JSON string representation of the object
print(APIGetCommentsResponse.to_json())

# convert the object into a dict
api_get_comments_response_dict = api_get_comments_response_instance.to_dict()
# create an instance of APIGetCommentsResponse from a dict
api_get_comments_response_from_dict = APIGetCommentsResponse.from_dict(api_get_comments_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


