# GetCommentsPublic200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **int** |  | [optional] 
**status** | [**ImportedAPIStatusFAILED**](ImportedAPIStatusFAILED.md) |  | 
**code** | **str** |  | 
**reason** | **str** |  | 
**translated_warning** | **str** |  | [optional] 
**comments** | [**List[PublicComment]**](PublicComment.md) |  | 
**user** | [**UserSessionInfo**](UserSessionInfo.md) |  | 
**url_id_clean** | **str** |  | [optional] 
**last_gen_date** | **int** |  | [optional] 
**includes_past_pages** | **bool** |  | [optional] 
**is_demo** | **bool** |  | [optional] 
**comment_count** | **int** |  | [optional] 
**is_site_admin** | **bool** |  | [optional] 
**has_billing_issue** | **bool** |  | [optional] 
**module_data** | **Dict[str, object]** | Construct a type with a set of properties K of type T | [optional] 
**page_number** | **int** |  | 
**is_white_labeled** | **bool** |  | [optional] 
**is_prod** | **bool** |  | [optional] 
**is_crawler** | **bool** |  | [optional] 
**notification_count** | **int** |  | [optional] 
**has_more** | **bool** |  | [optional] 
**is_closed** | **bool** |  | [optional] 
**presence_poll_state** | **int** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 
**url_id_ws** | **str** |  | [optional] 
**user_id_ws** | **str** |  | [optional] 
**tenant_id_ws** | **str** |  | [optional] 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 

## Example

```python
from client.models.get_comments_public200_response import GetCommentsPublic200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetCommentsPublic200Response from a JSON string
get_comments_public200_response_instance = GetCommentsPublic200Response.from_json(json)
# print the JSON string representation of the object
print(GetCommentsPublic200Response.to_json())

# convert the object into a dict
get_comments_public200_response_dict = get_comments_public200_response_instance.to_dict()
# create an instance of GetCommentsPublic200Response from a dict
get_comments_public200_response_from_dict = GetCommentsPublic200Response.from_dict(get_comments_public200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


