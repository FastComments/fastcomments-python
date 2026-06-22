# UpdateQuestionConfigResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**APIStatus**](APIStatus.md) |  | 
**reason** | **str** |  | 
**code** | **str** |  | 
**secondary_code** | **str** |  | [optional] 
**banned_until** | **int** |  | [optional] 
**max_character_length** | **int** |  | [optional] 
**translated_error** | **str** |  | [optional] 
**custom_config** | [**CustomConfigParameters**](CustomConfigParameters.md) |  | [optional] 

## Example

```python
from client.models.update_question_config_response import UpdateQuestionConfigResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateQuestionConfigResponse from a JSON string
update_question_config_response_instance = UpdateQuestionConfigResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateQuestionConfigResponse.to_json())

# convert the object into a dict
update_question_config_response_dict = update_question_config_response_instance.to_dict()
# create an instance of UpdateQuestionConfigResponse from a dict
update_question_config_response_from_dict = UpdateQuestionConfigResponse.from_dict(update_question_config_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


