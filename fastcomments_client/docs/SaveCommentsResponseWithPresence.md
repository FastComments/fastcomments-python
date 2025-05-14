# SaveCommentsResponseWithPresence


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ImportedAPIStatusSUCCESS**](ImportedAPIStatusSUCCESS.md) |  | 
**comment** | [**PublicComment**](PublicComment.md) |  | 
**user** | [**UserSessionInfo**](UserSessionInfo.md) |  | 
**module_data** | **Dict[str, object]** | Construct a type with a set of properties K of type T | [optional] 
**user_id_ws** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.save_comments_response_with_presence import SaveCommentsResponseWithPresence

# TODO update the JSON string below
json = "{}"
# create an instance of SaveCommentsResponseWithPresence from a JSON string
save_comments_response_with_presence_instance = SaveCommentsResponseWithPresence.from_json(json)
# print the JSON string representation of the object
print(SaveCommentsResponseWithPresence.to_json())

# convert the object into a dict
save_comments_response_with_presence_dict = save_comments_response_with_presence_instance.to_dict()
# create an instance of SaveCommentsResponseWithPresence from a dict
save_comments_response_with_presence_from_dict = SaveCommentsResponseWithPresence.from_dict(save_comments_response_with_presence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


