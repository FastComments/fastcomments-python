# CreateQuestionConfigResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**question_config** | [**QuestionConfig**](QuestionConfig.md) |  | 

## Example

```python
from client.models.create_question_config_response import CreateQuestionConfigResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateQuestionConfigResponse from a JSON string
create_question_config_response_instance = CreateQuestionConfigResponse.from_json(json)
# print the JSON string representation of the object
print(CreateQuestionConfigResponse.to_json())

# convert the object into a dict
create_question_config_response_dict = create_question_config_response_instance.to_dict()
# create an instance of CreateQuestionConfigResponse from a dict
create_question_config_response_from_dict = CreateQuestionConfigResponse.from_dict(create_question_config_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


