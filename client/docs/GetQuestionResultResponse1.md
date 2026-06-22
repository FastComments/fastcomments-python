# GetQuestionResultResponse1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**question_result** | [**QuestionResult**](QuestionResult.md) |  | 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.get_question_result_response1 import GetQuestionResultResponse1

# TODO update the JSON string below
json = "{}"
# create an instance of GetQuestionResultResponse1 from a JSON string
get_question_result_response1_instance = GetQuestionResultResponse1.from_json(json)
# print the JSON string representation of the object
print(GetQuestionResultResponse1.to_json())

# convert the object into a dict
get_question_result_response1_dict = get_question_result_response1_instance.to_dict()
# create an instance of GetQuestionResultResponse1 from a dict
get_question_result_response1_from_dict = GetQuestionResultResponse1.from_dict(get_question_result_response1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


