# QuestionConfigCustomOptionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_src** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from client.models.question_config_custom_options_inner import QuestionConfigCustomOptionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of QuestionConfigCustomOptionsInner from a JSON string
question_config_custom_options_inner_instance = QuestionConfigCustomOptionsInner.from_json(json)
# print the JSON string representation of the object
print(QuestionConfigCustomOptionsInner.to_json())

# convert the object into a dict
question_config_custom_options_inner_dict = question_config_custom_options_inner_instance.to_dict()
# create an instance of QuestionConfigCustomOptionsInner from a dict
question_config_custom_options_inner_from_dict = QuestionConfigCustomOptionsInner.from_dict(question_config_custom_options_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


