# CustomConfigParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**absolute_and_relative_dates** | **bool** |  | [optional] 
**absolute_dates** | **bool** |  | [optional] 
**allow_anon** | **bool** |  | [optional] 
**allow_anon_flag** | **bool** |  | [optional] 
**allow_anon_votes** | **bool** |  | [optional] 
**allowed_languages** | **List[str]** |  | [optional] 
**collapse_replies** | **bool** |  | [optional] 
**comment_count_format** | **str** |  | [optional] 
**comment_html_rendering_mode** | [**CommentHTMLRenderingMode**](CommentHTMLRenderingMode.md) |  | [optional] 
**comment_thread_delete_mode** | [**CommentThreadDeletionMode**](CommentThreadDeletionMode.md) |  | [optional] 
**commenter_name_format** | [**CommenterNameFormats**](CommenterNameFormats.md) |  | [optional] 
**count_above_toggle** | **int** |  | [optional] 
**custom_css** | **str** |  | [optional] 
**default_avatar_src** | **str** |  | [optional] 
**default_sort_direction** | [**SortDirections**](SortDirections.md) |  | [optional] 
**default_username** | **str** |  | [optional] 
**disable_auto_admin_migration** | **bool** |  | [optional] 
**disable_auto_hash_tag_creation** | **bool** |  | [optional] 
**disable_blocking** | **bool** |  | [optional] 
**disable_commenter_comment_delete** | **bool** |  | [optional] 
**disable_commenter_comment_edit** | **bool** |  | [optional] 
**disable_email_inputs** | **bool** |  | [optional] 
**disable_live_commenting** | **bool** |  | [optional] 
**disable_notification_bell** | **bool** |  | [optional] 
**disable_profiles** | **bool** |  | [optional] 
**disable_success_message** | **bool** |  | [optional] 
**disable_toolbar** | **bool** |  | [optional] 
**disable_unverified_label** | **bool** |  | [optional] 
**disable_voting** | **bool** |  | [optional] 
**enable_commenter_links** | **bool** |  | [optional] 
**enable_search** | **bool** |  | [optional] 
**enable_spoilers** | **bool** |  | [optional] 
**enable_third_party_cookie_bypass** | **bool** |  | [optional] 
**enable_view_counts** | **bool** |  | [optional] 
**enable_vote_list** | **bool** |  | [optional] 
**enable_wysiwyg** | **bool** |  | [optional] 
**gif_rating** | [**GifRating**](GifRating.md) |  | [optional] 
**has_dark_background** | **bool** |  | [optional] 
**header_html** | **str** |  | [optional] 
**hide_avatars** | **bool** |  | [optional] 
**hide_comments_under_count_text_format** | **str** |  | [optional] 
**image_content_profanity_level** | [**ImageContentProfanityLevel**](ImageContentProfanityLevel.md) |  | [optional] 
**input_after_comments** | **bool** |  | [optional] 
**limit_comments_by_groups** | **bool** |  | [optional] 
**locale** | **str** |  | [optional] 
**max_comment_character_length** | **int** |  | [optional] 
**max_comment_created_count_pupm** | **int** |  | [optional] 
**no_custom_config** | **bool** |  | [optional] 
**no_image_uploads** | **bool** |  | [optional] 
**no_styles** | **bool** |  | [optional] 
**page_size** | **int** |  | [optional] 
**readonly** | **bool** |  | [optional] 
**no_new_root_comments** | **bool** |  | [optional] 
**require_sso** | **bool** |  | [optional] 
**enable_resize_handle** | **bool** |  | [optional] 
**restricted_link_domains** | **List[str]** |  | [optional] 
**show_badges_in_top_bar** | **bool** |  | [optional] 
**show_comment_save_success** | **bool** |  | [optional] 
**show_live_right_away** | **bool** |  | [optional] 
**show_question** | **bool** |  | [optional] 
**spam_rules** | [**List[SpamRule]**](SpamRule.md) |  | [optional] 
**sso_sec_lvl** | [**SSOSecurityLevel**](SSOSecurityLevel.md) |  | [optional] 
**translations** | **Dict[str, str]** | Construct a type with a set of properties K of type T | [optional] 
**use_show_comments_toggle** | **bool** |  | [optional] 
**use_single_line_comment_input** | **bool** |  | [optional] 
**vote_style** | [**VoteStyle**](VoteStyle.md) |  | [optional] 
**widget_question_id** | **str** |  | [optional] 
**widget_question_results_style** | [**CommentQuestionResultsRenderingType**](CommentQuestionResultsRenderingType.md) |  | [optional] 
**widget_question_style** | [**QuestionRenderingType**](QuestionRenderingType.md) |  | [optional] 
**widget_question_when_to_save** | [**QuestionWhenSave**](QuestionWhenSave.md) |  | [optional] 
**widget_questions_required** | [**CommentQuestionsRequired**](CommentQuestionsRequired.md) |  | [optional] 
**widget_sub_question_visibility** | [**QuestionSubQuestionVisibility**](QuestionSubQuestionVisibility.md) |  | [optional] 
**wrap** | **bool** |  | [optional] 

## Example

```python
from client.models.custom_config_parameters import CustomConfigParameters

# TODO update the JSON string below
json = "{}"
# create an instance of CustomConfigParameters from a JSON string
custom_config_parameters_instance = CustomConfigParameters.from_json(json)
# print the JSON string representation of the object
print(CustomConfigParameters.to_json())

# convert the object into a dict
custom_config_parameters_dict = custom_config_parameters_instance.to_dict()
# create an instance of CustomConfigParameters from a dict
custom_config_parameters_from_dict = CustomConfigParameters.from_dict(custom_config_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


