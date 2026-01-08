# GetQuestionConfigResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**question_config** | [**QuestionConfig**](QuestionConfig.md) |  | 

## Example

```python
from client.models.get_question_config_response import GetQuestionConfigResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetQuestionConfigResponse from a JSON string
get_question_config_response_instance = GetQuestionConfigResponse.from_json(json)
# print the JSON string representation of the object
print(GetQuestionConfigResponse.to_json())

# convert the object into a dict
get_question_config_response_dict = get_question_config_response_instance.to_dict()
# create an instance of GetQuestionConfigResponse from a dict
get_question_config_response_from_dict = GetQuestionConfigResponse.from_dict(get_question_config_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


