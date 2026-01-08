# CreateQuestionResultBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url_id** | **str** |  | 
**value** | **float** |  | 
**question_id** | **str** |  | 
**anon_user_id** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**comment_id** | **str** |  | [optional] 
**meta** | [**List[MetaItem]**](MetaItem.md) |  | [optional] 

## Example

```python
from client.models.create_question_result_body import CreateQuestionResultBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreateQuestionResultBody from a JSON string
create_question_result_body_instance = CreateQuestionResultBody.from_json(json)
# print the JSON string representation of the object
print(CreateQuestionResultBody.to_json())

# convert the object into a dict
create_question_result_body_dict = create_question_result_body_instance.to_dict()
# create an instance of CreateQuestionResultBody from a dict
create_question_result_body_from_dict = CreateQuestionResultBody.from_dict(create_question_result_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


