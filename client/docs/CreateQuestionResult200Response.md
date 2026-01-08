# CreateQuestionResult200Response


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
from client.models.create_question_result200_response import CreateQuestionResult200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateQuestionResult200Response from a JSON string
create_question_result200_response_instance = CreateQuestionResult200Response.from_json(json)
# print the JSON string representation of the object
print(CreateQuestionResult200Response.to_json())

# convert the object into a dict
create_question_result200_response_dict = create_question_result200_response_instance.to_dict()
# create an instance of CreateQuestionResult200Response from a dict
create_question_result200_response_from_dict = CreateQuestionResult200Response.from_dict(create_question_result200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


