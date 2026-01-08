# CreateQuestionConfigBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**question** | **str** |  | 
**help_text** | **str** |  | [optional] 
**type** | **str** |  | 
**num_stars** | **float** |  | [optional] 
**min** | **float** |  | [optional] 
**max** | **float** |  | [optional] 
**default_value** | **float** |  | [optional] 
**label_negative** | **str** |  | [optional] 
**label_positive** | **str** |  | [optional] 
**custom_options** | [**List[QuestionConfigCustomOptionsInner]**](QuestionConfigCustomOptionsInner.md) |  | [optional] 
**sub_question_ids** | **List[str]** |  | [optional] 
**always_show_sub_questions** | **bool** |  | [optional] 
**reporting_order** | **float** |  | 

## Example

```python
from client.models.create_question_config_body import CreateQuestionConfigBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreateQuestionConfigBody from a JSON string
create_question_config_body_instance = CreateQuestionConfigBody.from_json(json)
# print the JSON string representation of the object
print(CreateQuestionConfigBody.to_json())

# convert the object into a dict
create_question_config_body_dict = create_question_config_body_instance.to_dict()
# create an instance of CreateQuestionConfigBody from a dict
create_question_config_body_from_dict = CreateQuestionConfigBody.from_dict(create_question_config_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


