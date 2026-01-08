# QuestionConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**name** | **str** |  | 
**question** | **str** |  | 
**summary_label** | **str** |  | [optional] 
**help_text** | **str** |  | 
**created_at** | **datetime** |  | 
**created_by** | **str** |  | 
**used_count** | **float** |  | 
**last_used** | **datetime** |  | 
**type** | **str** |  | 
**num_stars** | **float** |  | 
**min** | **float** |  | 
**max** | **float** |  | 
**default_value** | **float** |  | 
**label_negative** | **str** |  | 
**label_positive** | **str** |  | 
**custom_options** | [**List[QuestionConfigCustomOptionsInner]**](QuestionConfigCustomOptionsInner.md) |  | 
**sub_question_ids** | **List[str]** |  | 
**always_show_sub_questions** | **bool** |  | 
**reporting_order** | **float** |  | 

## Example

```python
from client.models.question_config import QuestionConfig

# TODO update the JSON string below
json = "{}"
# create an instance of QuestionConfig from a JSON string
question_config_instance = QuestionConfig.from_json(json)
# print the JSON string representation of the object
print(QuestionConfig.to_json())

# convert the object into a dict
question_config_dict = question_config_instance.to_dict()
# create an instance of QuestionConfig from a dict
question_config_from_dict = QuestionConfig.from_dict(question_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


