# CreateCommentPublic200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**comment** | [**PublicComment**](PublicComment.md) |  | 
**user** | [**UserSessionInfo**](UserSessionInfo.md) |  | 
**module_data** | **Dict[str, object]** | Construct a type with a set of properties K of type T | [optional] 
**user_id_ws** | **str** |  | [optional] 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.create_comment_public200_response import CreateCommentPublic200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCommentPublic200Response from a JSON string
create_comment_public200_response_instance = CreateCommentPublic200Response.from_json(json)
# print the JSON string representation of the object
print(CreateCommentPublic200Response.to_json())

# convert the object into a dict
create_comment_public200_response_dict = create_comment_public200_response_instance.to_dict()
# create an instance of CreateCommentPublic200Response from a dict
create_comment_public200_response_from_dict = CreateCommentPublic200Response.from_dict(create_comment_public200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


