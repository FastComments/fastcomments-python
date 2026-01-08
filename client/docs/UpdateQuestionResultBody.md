# UpdateQuestionResultBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url_id** | **str** |  | [optional] 
**anon_user_id** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**value** | **float** |  | [optional] 
**comment_id** | **str** |  | [optional] 
**question_id** | **str** |  | [optional] 
**meta** | [**List[MetaItem]**](MetaItem.md) |  | [optional] 

## Example

```python
from client.models.update_question_result_body import UpdateQuestionResultBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateQuestionResultBody from a JSON string
update_question_result_body_instance = UpdateQuestionResultBody.from_json(json)
# print the JSON string representation of the object
print(UpdateQuestionResultBody.to_json())

# convert the object into a dict
update_question_result_body_dict = update_question_result_body_instance.to_dict()
# create an instance of UpdateQuestionResultBody from a dict
update_question_result_body_from_dict = UpdateQuestionResultBody.from_dict(update_question_result_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


