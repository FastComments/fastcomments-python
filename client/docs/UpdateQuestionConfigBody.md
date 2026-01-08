# UpdateQuestionConfigBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**question** | **str** |  | [optional] 
**help_text** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**num_stars** | **float** |  | [optional] 
**min** | **float** |  | [optional] 
**max** | **float** |  | [optional] 
**default_value** | **float** |  | [optional] 
**label_negative** | **str** |  | [optional] 
**label_positive** | **str** |  | [optional] 
**custom_options** | [**List[QuestionConfigCustomOptionsInner]**](QuestionConfigCustomOptionsInner.md) |  | [optional] 
**sub_question_ids** | **List[str]** |  | [optional] 
**always_show_sub_questions** | **bool** |  | [optional] 
**reporting_order** | **float** |  | [optional] 

## Example

```python
from client.models.update_question_config_body import UpdateQuestionConfigBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateQuestionConfigBody from a JSON string
update_question_config_body_instance = UpdateQuestionConfigBody.from_json(json)
# print the JSON string representation of the object
print(UpdateQuestionConfigBody.to_json())

# convert the object into a dict
update_question_config_body_dict = update_question_config_body_instance.to_dict()
# create an instance of UpdateQuestionConfigBody from a dict
update_question_config_body_from_dict = UpdateQuestionConfigBody.from_dict(update_question_config_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


