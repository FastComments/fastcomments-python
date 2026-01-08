# GetQuestionConfigsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**question_configs** | [**List[QuestionConfig]**](QuestionConfig.md) |  | 

## Example

```python
from client.models.get_question_configs_response import GetQuestionConfigsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetQuestionConfigsResponse from a JSON string
get_question_configs_response_instance = GetQuestionConfigsResponse.from_json(json)
# print the JSON string representation of the object
print(GetQuestionConfigsResponse.to_json())

# convert the object into a dict
get_question_configs_response_dict = get_question_configs_response_instance.to_dict()
# create an instance of GetQuestionConfigsResponse from a dict
get_question_configs_response_from_dict = GetQuestionConfigsResponse.from_dict(get_question_configs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


