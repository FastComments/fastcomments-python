# CreateQuestionConfigResponse1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**question_config** | [**QuestionConfig**](QuestionConfig.md) |  | 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.create_question_config_response1 import CreateQuestionConfigResponse1

# TODO update the JSON string below
json = "{}"
# create an instance of CreateQuestionConfigResponse1 from a JSON string
create_question_config_response1_instance = CreateQuestionConfigResponse1.from_json(json)
# print the JSON string representation of the object
print(CreateQuestionConfigResponse1.to_json())

# convert the object into a dict
create_question_config_response1_dict = create_question_config_response1_instance.to_dict()
# create an instance of CreateQuestionConfigResponse1 from a dict
create_question_config_response1_from_dict = CreateQuestionConfigResponse1.from_dict(create_question_config_response1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


