# generated.PublicApi

All URIs are relative to *https://fastcomments.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**block_from_comment_public**](PublicApi.md#block_from_comment_public) | **POST** /block-from-comment/{commentId} | 
[**checked_comments_for_blocked**](PublicApi.md#checked_comments_for_blocked) | **GET** /check-blocked-comments | 
[**create_comment_public**](PublicApi.md#create_comment_public) | **POST** /comments/{tenantId} | 
[**create_feed_post_public**](PublicApi.md#create_feed_post_public) | **POST** /feed-posts/{tenantId} | 
[**delete_comment_public**](PublicApi.md#delete_comment_public) | **DELETE** /comments/{tenantId}/{commentId} | 
[**delete_comment_vote**](PublicApi.md#delete_comment_vote) | **DELETE** /comments/{tenantId}/{commentId}/vote/{voteId} | 
[**delete_feed_post_public**](PublicApi.md#delete_feed_post_public) | **DELETE** /feed-posts/{tenantId}/{postId} | 
[**flag_comment_public**](PublicApi.md#flag_comment_public) | **POST** /flag-comment/{commentId} | 
[**get_comment_text**](PublicApi.md#get_comment_text) | **GET** /comments/{tenantId}/{commentId}/text | 
[**get_comment_vote_user_names**](PublicApi.md#get_comment_vote_user_names) | **GET** /comments/{tenantId}/{commentId}/votes | 
[**get_comments_public**](PublicApi.md#get_comments_public) | **GET** /comments/{tenantId} | 
[**get_event_log**](PublicApi.md#get_event_log) | **GET** /event-log/{tenantId} | 
[**get_feed_posts_public**](PublicApi.md#get_feed_posts_public) | **GET** /feed-posts/{tenantId} | 
[**get_feed_posts_stats**](PublicApi.md#get_feed_posts_stats) | **GET** /feed-posts/{tenantId}/stats | 
[**get_global_event_log**](PublicApi.md#get_global_event_log) | **GET** /event-log/global/{tenantId} | 
[**get_user_notification_count**](PublicApi.md#get_user_notification_count) | **GET** /user-notifications/get-count | 
[**get_user_notifications**](PublicApi.md#get_user_notifications) | **GET** /user-notifications | 
[**get_user_presence_statuses**](PublicApi.md#get_user_presence_statuses) | **GET** /user-presence-status | 
[**get_user_reacts_public**](PublicApi.md#get_user_reacts_public) | **GET** /feed-posts/{tenantId}/user-reacts | 
[**lock_comment**](PublicApi.md#lock_comment) | **POST** /comments/{tenantId}/{commentId}/lock | 
[**pin_comment**](PublicApi.md#pin_comment) | **POST** /comments/{tenantId}/{commentId}/pin | 
[**react_feed_post_public**](PublicApi.md#react_feed_post_public) | **POST** /feed-posts/{tenantId}/react/{postId} | 
[**reset_user_notification_count**](PublicApi.md#reset_user_notification_count) | **POST** /user-notifications/reset-count | 
[**reset_user_notifications**](PublicApi.md#reset_user_notifications) | **POST** /user-notifications/reset | 
[**search_users**](PublicApi.md#search_users) | **GET** /user-search/{tenantId} | 
[**set_comment_text**](PublicApi.md#set_comment_text) | **POST** /comments/{tenantId}/{commentId}/update-text | 
[**un_block_comment_public**](PublicApi.md#un_block_comment_public) | **DELETE** /block-from-comment/{commentId} | 
[**un_lock_comment**](PublicApi.md#un_lock_comment) | **POST** /comments/{tenantId}/{commentId}/unlock | 
[**un_pin_comment**](PublicApi.md#un_pin_comment) | **POST** /comments/{tenantId}/{commentId}/unpin | 
[**update_feed_post_public**](PublicApi.md#update_feed_post_public) | **PUT** /feed-posts/{tenantId}/{postId} | 
[**update_user_notification_comment_subscription_status**](PublicApi.md#update_user_notification_comment_subscription_status) | **POST** /user-notifications/{notificationId}/mark-opted/{optedInOrOut} | 
[**update_user_notification_page_subscription_status**](PublicApi.md#update_user_notification_page_subscription_status) | **POST** /user-notifications/set-subscription-state/{subscribedOrUnsubscribed} | 
[**update_user_notification_status**](PublicApi.md#update_user_notification_status) | **POST** /user-notifications/{notificationId}/mark/{newStatus} | 
[**upload_image**](PublicApi.md#upload_image) | **POST** /upload-image/{tenantId} | 
[**vote_comment**](PublicApi.md#vote_comment) | **POST** /comments/{tenantId}/{commentId}/vote | 


# **block_from_comment_public**
> BlockFromCommentPublic200Response block_from_comment_public(tenant_id, comment_id, public_block_from_comment_params, sso=sso)



### Example


```python
import generated
from generated.models.block_from_comment_public200_response import BlockFromCommentPublic200Response
from generated.models.public_block_from_comment_params import PublicBlockFromCommentParams
from generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = generated.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = generated.PublicApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    comment_id = 'comment_id_example' # str | 
    public_block_from_comment_params = generated.PublicBlockFromCommentParams() # PublicBlockFromCommentParams | 
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.block_from_comment_public(tenant_id, comment_id, public_block_from_comment_params, sso=sso)
        print("The response of PublicApi->block_from_comment_public:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->block_from_comment_public: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **comment_id** | **str**|  | 
 **public_block_from_comment_params** | [**PublicBlockFromCommentParams**](PublicBlockFromCommentParams.md)|  | 
 **sso** | **str**|  | [optional] 

### Return type

[**BlockFromCommentPublic200Response**](BlockFromCommentPublic200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checked_comments_for_blocked**
> CheckedCommentsForBlocked200Response checked_comments_for_blocked(tenant_id, comment_ids, sso=sso)



### Example


```python
import generated
from generated.models.checked_comments_for_blocked200_response import CheckedCommentsForBlocked200Response
from generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = generated.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = generated.PublicApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    comment_ids = 'comment_ids_example' # str | A comma separated list of comment ids.
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.checked_comments_for_blocked(tenant_id, comment_ids, sso=sso)
        print("The response of PublicApi->checked_comments_for_blocked:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->checked_comments_for_blocked: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **comment_ids** | **str**| A comma separated list of comment ids. | 
 **sso** | **str**|  | [optional] 

### Return type

[**CheckedCommentsForBlocked200Response**](CheckedCommentsForBlocked200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_comment_public**
> CreateCommentPublic200Response create_comment_public(tenant_id, url_id, broadcast_id, comment_data, session_id=session_id, sso=sso)



### Example


```python
import generated
from generated.models.comment_data import CommentData
from generated.models.create_comment_public200_response import CreateCommentPublic200Response
from generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = generated.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = generated.PublicApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    url_id = 'url_id_example' # str | 
    broadcast_id = 'broadcast_id_example' # str | 
    comment_data = generated.CommentData() # CommentData | 
    session_id = 'session_id_example' # str |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.create_comment_public(tenant_id, url_id, broadcast_id, comment_data, session_id=session_id, sso=sso)
        print("The response of PublicApi->create_comment_public:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->create_comment_public: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **url_id** | **str**|  | 
 **broadcast_id** | **str**|  | 
 **comment_data** | [**CommentData**](CommentData.md)|  | 
 **session_id** | **str**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**CreateCommentPublic200Response**](CreateCommentPublic200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_feed_post_public**
> CreateFeedPostPublic200Response create_feed_post_public(tenant_id, create_feed_post_params, broadcast_id=broadcast_id, sso=sso)



### Example


```python
import generated
from generated.models.create_feed_post_params import CreateFeedPostParams
from generated.models.create_feed_post_public200_response import CreateFeedPostPublic200Response
from generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = generated.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = generated.PublicApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    create_feed_post_params = generated.CreateFeedPostParams() # CreateFeedPostParams | 
    broadcast_id = 'broadcast_id_example' # str |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.create_feed_post_public(tenant_id, create_feed_post_params, broadcast_id=broadcast_id, sso=sso)
        print("The response of PublicApi->create_feed_post_public:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->create_feed_post_public: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **create_feed_post_params** | [**CreateFeedPostParams**](CreateFeedPostParams.md)|  | 
 **broadcast_id** | **str**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**CreateFeedPostPublic200Response**](CreateFeedPostPublic200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_comment_public**
> DeleteCommentPublic200Response delete_comment_public(tenant_id, comment_id, broadcast_id, edit_key=edit_key, sso=sso)



### Example


```python
import generated
from generated.models.delete_comment_public200_response import DeleteCommentPublic200Response
from generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = generated.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = generated.PublicApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    comment_id = 'comment_id_example' # str | 
    broadcast_id = 'broadcast_id_example' # str | 
    edit_key = 'edit_key_example' # str |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.delete_comment_public(tenant_id, comment_id, broadcast_id, edit_key=edit_key, sso=sso)
        print("The response of PublicApi->delete_comment_public:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->delete_comment_public: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **comment_id** | **str**|  | 
 **broadcast_id** | **str**|  | 
 **edit_key** | **str**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**DeleteCommentPublic200Response**](DeleteCommentPublic200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_comment_vote**
> DeleteCommentVote200Response delete_comment_vote(tenant_id, comment_id, vote_id, url_id, broadcast_id, edit_key=edit_key, sso=sso)



### Example


```python
import generated
from generated.models.delete_comment_vote200_response import DeleteCommentVote200Response
from generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = generated.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = generated.PublicApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    comment_id = 'comment_id_example' # str | 
    vote_id = 'vote_id_example' # str | 
    url_id = 'url_id_example' # str | 
    broadcast_id = 'broadcast_id_example' # str | 
    edit_key = 'edit_key_example' # str |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.delete_comment_vote(tenant_id, comment_id, vote_id, url_id, broadcast_id, edit_key=edit_key, sso=sso)
        print("The response of PublicApi->delete_comment_vote:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->delete_comment_vote: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **comment_id** | **str**|  | 
 **vote_id** | **str**|  | 
 **url_id** | **str**|  | 
 **broadcast_id** | **str**|  | 
 **edit_key** | **str**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**DeleteCommentVote200Response**](DeleteCommentVote200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_feed_post_public**
> DeleteFeedPostPublic200Response delete_feed_post_public(tenant_id, post_id, broadcast_id=broadcast_id, sso=sso)



### Example


```python
import generated
from generated.models.delete_feed_post_public200_response import DeleteFeedPostPublic200Response
from generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = generated.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = generated.PublicApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    post_id = 'post_id_example' # str | 
    broadcast_id = 'broadcast_id_example' # str |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.delete_feed_post_public(tenant_id, post_id, broadcast_id=broadcast_id, sso=sso)
        print("The response of PublicApi->delete_feed_post_public:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->delete_feed_post_public: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **post_id** | **str**|  | 
 **broadcast_id** | **str**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**DeleteFeedPostPublic200Response**](DeleteFeedPostPublic200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **flag_comment_public**
> FlagCommentPublic200Response flag_comment_public(tenant_id, comment_id, is_flagged, sso=sso)



### Example


```python
import generated
from generated.models.flag_comment_public200_response import FlagCommentPublic200Response
from generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = generated.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = generated.PublicApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    comment_id = 'comment_id_example' # str | 
    is_flagged = True # bool | 
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.flag_comment_public(tenant_id, comment_id, is_flagged, sso=sso)
        print("The response of PublicApi->flag_comment_public:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->flag_comment_public: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **comment_id** | **str**|  | 
 **is_flagged** | **bool**|  | 
 **sso** | **str**|  | [optional] 

### Return type

[**FlagCommentPublic200Response**](FlagCommentPublic200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comment_text**
> GetCommentText200Response get_comment_text(tenant_id, comment_id, edit_key=edit_key, sso=sso)



### Example


```python
import generated
from generated.models.get_comment_text200_response import GetCommentText200Response
from generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = generated.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = generated.PublicApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    comment_id = 'comment_id_example' # str | 
    edit_key = 'edit_key_example' # str |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.get_comment_text(tenant_id, comment_id, edit_key=edit_key, sso=sso)
        print("The response of PublicApi->get_comment_text:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->get_comment_text: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **comment_id** | **str**|  | 
 **edit_key** | **str**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**GetCommentText200Response**](GetCommentText200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comment_vote_user_names**
> GetCommentVoteUserNames200Response get_comment_vote_user_names(tenant_id, comment_id, dir, sso=sso)



### Example


```python
import generated
from generated.models.get_comment_vote_user_names200_response import GetCommentVoteUserNames200Response
from generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = generated.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = generated.PublicApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    comment_id = 'comment_id_example' # str | 
    dir = 56 # int | 
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.get_comment_vote_user_names(tenant_id, comment_id, dir, sso=sso)
        print("The response of PublicApi->get_comment_vote_user_names:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->get_comment_vote_user_names: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **comment_id** | **str**|  | 
 **dir** | **int**|  | 
 **sso** | **str**|  | [optional] 

### Return type

[**GetCommentVoteUserNames200Response**](GetCommentVoteUserNames200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comments_public**
> GetCommentsPublic200Response get_comments_public(tenant_id, url_id, page=page, direction=direction, sso=sso, skip=skip, skip_children=skip_children, limit=limit, limit_children=limit_children, count_children=count_children, fetch_page_for_comment_id=fetch_page_for_comment_id, include_config=include_config, count_all=count_all, includei10n=includei10n, locale=locale, modules=modules, is_crawler=is_crawler, include_notification_count=include_notification_count, as_tree=as_tree, max_tree_depth=max_tree_depth, use_full_translation_ids=use_full_translation_ids, parent_id=parent_id, search_text=search_text, hash_tags=hash_tags, user_id=user_id, custom_config_str=custom_config_str, after_comment_id=after_comment_id, before_comment_id=before_comment_id)



 req tenantId urlId

### Example


```python
import generated
from generated.models.get_comments_public200_response import GetCommentsPublic200Response
from generated.models.sort_directions import SortDirections
from generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = generated.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = generated.PublicApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    url_id = 'url_id_example' # str | 
    page = 56 # int |  (optional)
    direction = generated.SortDirections() # SortDirections |  (optional)
    sso = 'sso_example' # str |  (optional)
    skip = 56 # int |  (optional)
    skip_children = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    limit_children = 56 # int |  (optional)
    count_children = True # bool |  (optional)
    fetch_page_for_comment_id = 'fetch_page_for_comment_id_example' # str |  (optional)
    include_config = True # bool |  (optional)
    count_all = True # bool |  (optional)
    includei10n = True # bool |  (optional)
    locale = 'locale_example' # str |  (optional)
    modules = 'modules_example' # str |  (optional)
    is_crawler = True # bool |  (optional)
    include_notification_count = True # bool |  (optional)
    as_tree = True # bool |  (optional)
    max_tree_depth = 56 # int |  (optional)
    use_full_translation_ids = True # bool |  (optional)
    parent_id = 'parent_id_example' # str |  (optional)
    search_text = 'search_text_example' # str |  (optional)
    hash_tags = ['hash_tags_example'] # List[str] |  (optional)
    user_id = 'user_id_example' # str |  (optional)
    custom_config_str = 'custom_config_str_example' # str |  (optional)
    after_comment_id = 'after_comment_id_example' # str |  (optional)
    before_comment_id = 'before_comment_id_example' # str |  (optional)

    try:
        api_response = api_instance.get_comments_public(tenant_id, url_id, page=page, direction=direction, sso=sso, skip=skip, skip_children=skip_children, limit=limit, limit_children=limit_children, count_children=count_children, fetch_page_for_comment_id=fetch_page_for_comment_id, include_config=include_config, count_all=count_all, includei10n=includei10n, locale=locale, modules=modules, is_crawler=is_crawler, include_notification_count=include_notification_count, as_tree=as_tree, max_tree_depth=max_tree_depth, use_full_translation_ids=use_full_translation_ids, parent_id=parent_id, search_text=search_text, hash_tags=hash_tags, user_id=user_id, custom_config_str=custom_config_str, after_comment_id=after_comment_id, before_comment_id=before_comment_id)
        print("The response of PublicApi->get_comments_public:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->get_comments_public: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **url_id** | **str**|  | 
 **page** | **int**|  | [optional] 
 **direction** | [**SortDirections**](.md)|  | [optional] 
 **sso** | **str**|  | [optional] 
 **skip** | **int**|  | [optional] 
 **skip_children** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **limit_children** | **int**|  | [optional] 
 **count_children** | **bool**|  | [optional] 
 **fetch_page_for_comment_id** | **str**|  | [optional] 
 **include_config** | **bool**|  | [optional] 
 **count_all** | **bool**|  | [optional] 
 **includei10n** | **bool**|  | [optional] 
 **locale** | **str**|  | [optional] 
 **modules** | **str**|  | [optional] 
 **is_crawler** | **bool**|  | [optional] 
 **include_notification_count** | **bool**|  | [optional] 
 **as_tree** | **bool**|  | [optional] 
 **max_tree_depth** | **int**|  | [optional] 
 **use_full_translation_ids** | **bool**|  | [optional] 
 **parent_id** | **str**|  | [optional] 
 **search_text** | **str**|  | [optional] 
 **hash_tags** | [**List[str]**](str.md)|  | [optional] 
 **user_id** | **str**|  | [optional] 
 **custom_config_str** | **str**|  | [optional] 
 **after_comment_id** | **str**|  | [optional] 
 **before_comment_id** | **str**|  | [optional] 

### Return type

[**GetCommentsPublic200Response**](GetCommentsPublic200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_log**
> GetEventLog200Response get_event_log(tenant_id, url_id, user_id_ws, start_time, end_time)



 req tenantId urlId userIdWS

### Example


```python
import generated
from generated.models.get_event_log200_response import GetEventLog200Response
from generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = generated.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = generated.PublicApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    url_id = 'url_id_example' # str | 
    user_id_ws = 'user_id_ws_example' # str | 
    start_time = 56 # int | 
    end_time = 56 # int | 

    try:
        api_response = api_instance.get_event_log(tenant_id, url_id, user_id_ws, start_time, end_time)
        print("The response of PublicApi->get_event_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->get_event_log: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **url_id** | **str**|  | 
 **user_id_ws** | **str**|  | 
 **start_time** | **int**|  | 
 **end_time** | **int**|  | 

### Return type

[**GetEventLog200Response**](GetEventLog200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feed_posts_public**
> GetFeedPostsPublic200Response get_feed_posts_public(tenant_id, after_id=after_id, limit=limit, tags=tags, sso=sso, is_crawler=is_crawler, include_user_info=include_user_info)



 req tenantId afterId

### Example


```python
import generated
from generated.models.get_feed_posts_public200_response import GetFeedPostsPublic200Response
from generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = generated.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = generated.PublicApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    after_id = 'after_id_example' # str |  (optional)
    limit = 56 # int |  (optional)
    tags = ['tags_example'] # List[str] |  (optional)
    sso = 'sso_example' # str |  (optional)
    is_crawler = True # bool |  (optional)
    include_user_info = True # bool |  (optional)

    try:
        api_response = api_instance.get_feed_posts_public(tenant_id, after_id=after_id, limit=limit, tags=tags, sso=sso, is_crawler=is_crawler, include_user_info=include_user_info)
        print("The response of PublicApi->get_feed_posts_public:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->get_feed_posts_public: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **after_id** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **tags** | [**List[str]**](str.md)|  | [optional] 
 **sso** | **str**|  | [optional] 
 **is_crawler** | **bool**|  | [optional] 
 **include_user_info** | **bool**|  | [optional] 

### Return type

[**GetFeedPostsPublic200Response**](GetFeedPostsPublic200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feed_posts_stats**
> GetFeedPostsStats200Response get_feed_posts_stats(tenant_id, post_ids, sso=sso)



### Example


```python
import generated
from generated.models.get_feed_posts_stats200_response import GetFeedPostsStats200Response
from generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = generated.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = generated.PublicApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    post_ids = ['post_ids_example'] # List[str] | 
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.get_feed_posts_stats(tenant_id, post_ids, sso=sso)
        print("The response of PublicApi->get_feed_posts_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->get_feed_posts_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **post_ids** | [**List[str]**](str.md)|  | 
 **sso** | **str**|  | [optional] 

### Return type

[**GetFeedPostsStats200Response**](GetFeedPostsStats200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_global_event_log**
> GetEventLog200Response get_global_event_log(tenant_id, url_id, user_id_ws, start_time, end_time)



 req tenantId urlId userIdWS

### Example


```python
import generated
from generated.models.get_event_log200_response import GetEventLog200Response
from generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = generated.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = generated.PublicApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    url_id = 'url_id_example' # str | 
    user_id_ws = 'user_id_ws_example' # str | 
    start_time = 56 # int | 
    end_time = 56 # int | 

    try:
        api_response = api_instance.get_global_event_log(tenant_id, url_id, user_id_ws, start_time, end_time)
        print("The response of PublicApi->get_global_event_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->get_global_event_log: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **url_id** | **str**|  | 
 **user_id_ws** | **str**|  | 
 **start_time** | **int**|  | 
 **end_time** | **int**|  | 

### Return type

[**GetEventLog200Response**](GetEventLog200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_notification_count**
> GetUserNotificationCount200Response get_user_notification_count(tenant_id, sso=sso)



### Example


```python
import generated
from generated.models.get_user_notification_count200_response import GetUserNotificationCount200Response
from generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = generated.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = generated.PublicApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.get_user_notification_count(tenant_id, sso=sso)
        print("The response of PublicApi->get_user_notification_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->get_user_notification_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **sso** | **str**|  | [optional] 

### Return type

[**GetUserNotificationCount200Response**](GetUserNotificationCount200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_notifications**
> GetUserNotifications200Response get_user_notifications(tenant_id, page_size=page_size, after_id=after_id, include_context=include_context, after_created_at=after_created_at, unread_only=unread_only, dm_only=dm_only, no_dm=no_dm, include_translations=include_translations, sso=sso)



### Example


```python
import generated
from generated.models.get_user_notifications200_response import GetUserNotifications200Response
from generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = generated.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = generated.PublicApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    page_size = 56 # int |  (optional)
    after_id = 'after_id_example' # str |  (optional)
    include_context = True # bool |  (optional)
    after_created_at = 56 # int |  (optional)
    unread_only = True # bool |  (optional)
    dm_only = True # bool |  (optional)
    no_dm = True # bool |  (optional)
    include_translations = True # bool |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.get_user_notifications(tenant_id, page_size=page_size, after_id=after_id, include_context=include_context, after_created_at=after_created_at, unread_only=unread_only, dm_only=dm_only, no_dm=no_dm, include_translations=include_translations, sso=sso)
        print("The response of PublicApi->get_user_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->get_user_notifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **page_size** | **int**|  | [optional] 
 **after_id** | **str**|  | [optional] 
 **include_context** | **bool**|  | [optional] 
 **after_created_at** | **int**|  | [optional] 
 **unread_only** | **bool**|  | [optional] 
 **dm_only** | **bool**|  | [optional] 
 **no_dm** | **bool**|  | [optional] 
 **include_translations** | **bool**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**GetUserNotifications200Response**](GetUserNotifications200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_presence_statuses**
> GetUserPresenceStatuses200Response get_user_presence_statuses(tenant_id, url_id_ws, user_ids)



### Example


```python
import generated
from generated.models.get_user_presence_statuses200_response import GetUserPresenceStatuses200Response
from generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = generated.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = generated.PublicApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    url_id_ws = 'url_id_ws_example' # str | 
    user_ids = 'user_ids_example' # str | 

    try:
        api_response = api_instance.get_user_presence_statuses(tenant_id, url_id_ws, user_ids)
        print("The response of PublicApi->get_user_presence_statuses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->get_user_presence_statuses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **url_id_ws** | **str**|  | 
 **user_ids** | **str**|  | 

### Return type

[**GetUserPresenceStatuses200Response**](GetUserPresenceStatuses200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**422** | Validation Failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_reacts_public**
> GetUserReactsPublic200Response get_user_reacts_public(tenant_id, post_ids=post_ids, sso=sso)



### Example


```python
import generated
from generated.models.get_user_reacts_public200_response import GetUserReactsPublic200Response
from generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = generated.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = generated.PublicApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    post_ids = ['post_ids_example'] # List[str] |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.get_user_reacts_public(tenant_id, post_ids=post_ids, sso=sso)
        print("The response of PublicApi->get_user_reacts_public:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->get_user_reacts_public: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **post_ids** | [**List[str]**](str.md)|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**GetUserReactsPublic200Response**](GetUserReactsPublic200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lock_comment**
> LockComment200Response lock_comment(tenant_id, comment_id, broadcast_id, sso=sso)



### Example


```python
import generated
from generated.models.lock_comment200_response import LockComment200Response
from generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = generated.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = generated.PublicApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    comment_id = 'comment_id_example' # str | 
    broadcast_id = 'broadcast_id_example' # str | 
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.lock_comment(tenant_id, comment_id, broadcast_id, sso=sso)
        print("The response of PublicApi->lock_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->lock_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **comment_id** | **str**|  | 
 **broadcast_id** | **str**|  | 
 **sso** | **str**|  | [optional] 

### Return type

[**LockComment200Response**](LockComment200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pin_comment**
> PinComment200Response pin_comment(tenant_id, comment_id, broadcast_id, sso=sso)



### Example


```python
import generated
from generated.models.pin_comment200_response import PinComment200Response
from generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = generated.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = generated.PublicApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    comment_id = 'comment_id_example' # str | 
    broadcast_id = 'broadcast_id_example' # str | 
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.pin_comment(tenant_id, comment_id, broadcast_id, sso=sso)
        print("The response of PublicApi->pin_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->pin_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **comment_id** | **str**|  | 
 **broadcast_id** | **str**|  | 
 **sso** | **str**|  | [optional] 

### Return type

[**PinComment200Response**](PinComment200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **react_feed_post_public**
> ReactFeedPostPublic200Response react_feed_post_public(tenant_id, post_id, react_body_params, is_undo=is_undo, broadcast_id=broadcast_id, sso=sso)



### Example


```python
import generated
from generated.models.react_body_params import ReactBodyParams
from generated.models.react_feed_post_public200_response import ReactFeedPostPublic200Response
from generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = generated.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = generated.PublicApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    post_id = 'post_id_example' # str | 
    react_body_params = generated.ReactBodyParams() # ReactBodyParams | 
    is_undo = True # bool |  (optional)
    broadcast_id = 'broadcast_id_example' # str |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.react_feed_post_public(tenant_id, post_id, react_body_params, is_undo=is_undo, broadcast_id=broadcast_id, sso=sso)
        print("The response of PublicApi->react_feed_post_public:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->react_feed_post_public: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **post_id** | **str**|  | 
 **react_body_params** | [**ReactBodyParams**](ReactBodyParams.md)|  | 
 **is_undo** | **bool**|  | [optional] 
 **broadcast_id** | **str**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**ReactFeedPostPublic200Response**](ReactFeedPostPublic200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_user_notification_count**
> ResetUserNotifications200Response reset_user_notification_count(tenant_id, sso=sso)



### Example


```python
import generated
from generated.models.reset_user_notifications200_response import ResetUserNotifications200Response
from generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = generated.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = generated.PublicApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.reset_user_notification_count(tenant_id, sso=sso)
        print("The response of PublicApi->reset_user_notification_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->reset_user_notification_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **sso** | **str**|  | [optional] 

### Return type

[**ResetUserNotifications200Response**](ResetUserNotifications200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_user_notifications**
> ResetUserNotifications200Response reset_user_notifications(tenant_id, after_id=after_id, after_created_at=after_created_at, unread_only=unread_only, dm_only=dm_only, no_dm=no_dm, sso=sso)



### Example


```python
import generated
from generated.models.reset_user_notifications200_response import ResetUserNotifications200Response
from generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = generated.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = generated.PublicApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    after_id = 'after_id_example' # str |  (optional)
    after_created_at = 56 # int |  (optional)
    unread_only = True # bool |  (optional)
    dm_only = True # bool |  (optional)
    no_dm = True # bool |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.reset_user_notifications(tenant_id, after_id=after_id, after_created_at=after_created_at, unread_only=unread_only, dm_only=dm_only, no_dm=no_dm, sso=sso)
        print("The response of PublicApi->reset_user_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->reset_user_notifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **after_id** | **str**|  | [optional] 
 **after_created_at** | **int**|  | [optional] 
 **unread_only** | **bool**|  | [optional] 
 **dm_only** | **bool**|  | [optional] 
 **no_dm** | **bool**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**ResetUserNotifications200Response**](ResetUserNotifications200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_users**
> SearchUsers200Response search_users(tenant_id, url_id, username_starts_with, mention_group_ids=mention_group_ids, sso=sso)



### Example


```python
import generated
from generated.models.search_users200_response import SearchUsers200Response
from generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = generated.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = generated.PublicApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    url_id = 'url_id_example' # str | 
    username_starts_with = 'username_starts_with_example' # str | 
    mention_group_ids = ['mention_group_ids_example'] # List[str] |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.search_users(tenant_id, url_id, username_starts_with, mention_group_ids=mention_group_ids, sso=sso)
        print("The response of PublicApi->search_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->search_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **url_id** | **str**|  | 
 **username_starts_with** | **str**|  | 
 **mention_group_ids** | [**List[str]**](str.md)|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**SearchUsers200Response**](SearchUsers200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_comment_text**
> SetCommentText200Response set_comment_text(tenant_id, comment_id, broadcast_id, comment_text_update_request, edit_key=edit_key, sso=sso)



### Example


```python
import generated
from generated.models.comment_text_update_request import CommentTextUpdateRequest
from generated.models.set_comment_text200_response import SetCommentText200Response
from generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = generated.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = generated.PublicApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    comment_id = 'comment_id_example' # str | 
    broadcast_id = 'broadcast_id_example' # str | 
    comment_text_update_request = generated.CommentTextUpdateRequest() # CommentTextUpdateRequest | 
    edit_key = 'edit_key_example' # str |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.set_comment_text(tenant_id, comment_id, broadcast_id, comment_text_update_request, edit_key=edit_key, sso=sso)
        print("The response of PublicApi->set_comment_text:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->set_comment_text: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **comment_id** | **str**|  | 
 **broadcast_id** | **str**|  | 
 **comment_text_update_request** | [**CommentTextUpdateRequest**](CommentTextUpdateRequest.md)|  | 
 **edit_key** | **str**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**SetCommentText200Response**](SetCommentText200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **un_block_comment_public**
> UnBlockCommentPublic200Response un_block_comment_public(tenant_id, comment_id, public_block_from_comment_params, sso=sso)



### Example


```python
import generated
from generated.models.public_block_from_comment_params import PublicBlockFromCommentParams
from generated.models.un_block_comment_public200_response import UnBlockCommentPublic200Response
from generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = generated.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = generated.PublicApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    comment_id = 'comment_id_example' # str | 
    public_block_from_comment_params = generated.PublicBlockFromCommentParams() # PublicBlockFromCommentParams | 
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.un_block_comment_public(tenant_id, comment_id, public_block_from_comment_params, sso=sso)
        print("The response of PublicApi->un_block_comment_public:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->un_block_comment_public: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **comment_id** | **str**|  | 
 **public_block_from_comment_params** | [**PublicBlockFromCommentParams**](PublicBlockFromCommentParams.md)|  | 
 **sso** | **str**|  | [optional] 

### Return type

[**UnBlockCommentPublic200Response**](UnBlockCommentPublic200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **un_lock_comment**
> LockComment200Response un_lock_comment(tenant_id, comment_id, broadcast_id, sso=sso)



### Example


```python
import generated
from generated.models.lock_comment200_response import LockComment200Response
from generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = generated.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = generated.PublicApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    comment_id = 'comment_id_example' # str | 
    broadcast_id = 'broadcast_id_example' # str | 
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.un_lock_comment(tenant_id, comment_id, broadcast_id, sso=sso)
        print("The response of PublicApi->un_lock_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->un_lock_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **comment_id** | **str**|  | 
 **broadcast_id** | **str**|  | 
 **sso** | **str**|  | [optional] 

### Return type

[**LockComment200Response**](LockComment200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **un_pin_comment**
> PinComment200Response un_pin_comment(tenant_id, comment_id, broadcast_id, sso=sso)



### Example


```python
import generated
from generated.models.pin_comment200_response import PinComment200Response
from generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = generated.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = generated.PublicApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    comment_id = 'comment_id_example' # str | 
    broadcast_id = 'broadcast_id_example' # str | 
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.un_pin_comment(tenant_id, comment_id, broadcast_id, sso=sso)
        print("The response of PublicApi->un_pin_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->un_pin_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **comment_id** | **str**|  | 
 **broadcast_id** | **str**|  | 
 **sso** | **str**|  | [optional] 

### Return type

[**PinComment200Response**](PinComment200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_feed_post_public**
> CreateFeedPostPublic200Response update_feed_post_public(tenant_id, post_id, update_feed_post_params, broadcast_id=broadcast_id, sso=sso)



### Example


```python
import generated
from generated.models.create_feed_post_public200_response import CreateFeedPostPublic200Response
from generated.models.update_feed_post_params import UpdateFeedPostParams
from generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = generated.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = generated.PublicApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    post_id = 'post_id_example' # str | 
    update_feed_post_params = generated.UpdateFeedPostParams() # UpdateFeedPostParams | 
    broadcast_id = 'broadcast_id_example' # str |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.update_feed_post_public(tenant_id, post_id, update_feed_post_params, broadcast_id=broadcast_id, sso=sso)
        print("The response of PublicApi->update_feed_post_public:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->update_feed_post_public: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **post_id** | **str**|  | 
 **update_feed_post_params** | [**UpdateFeedPostParams**](UpdateFeedPostParams.md)|  | 
 **broadcast_id** | **str**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**CreateFeedPostPublic200Response**](CreateFeedPostPublic200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_notification_comment_subscription_status**
> UpdateUserNotificationStatus200Response update_user_notification_comment_subscription_status(tenant_id, notification_id, opted_in_or_out, comment_id, sso=sso)



Enable or disable notifications for a specific comment.

### Example


```python
import generated
from generated.models.update_user_notification_status200_response import UpdateUserNotificationStatus200Response
from generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = generated.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = generated.PublicApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    notification_id = 'notification_id_example' # str | 
    opted_in_or_out = 'opted_in_or_out_example' # str | 
    comment_id = 'comment_id_example' # str | 
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.update_user_notification_comment_subscription_status(tenant_id, notification_id, opted_in_or_out, comment_id, sso=sso)
        print("The response of PublicApi->update_user_notification_comment_subscription_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->update_user_notification_comment_subscription_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **notification_id** | **str**|  | 
 **opted_in_or_out** | **str**|  | 
 **comment_id** | **str**|  | 
 **sso** | **str**|  | [optional] 

### Return type

[**UpdateUserNotificationStatus200Response**](UpdateUserNotificationStatus200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_notification_page_subscription_status**
> UpdateUserNotificationStatus200Response update_user_notification_page_subscription_status(tenant_id, url_id, url, page_title, subscribed_or_unsubscribed, sso=sso)



Enable or disable notifications for a page. When users are subscribed to a page, notifications are created for new root comments, and also

### Example


```python
import generated
from generated.models.update_user_notification_status200_response import UpdateUserNotificationStatus200Response
from generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = generated.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = generated.PublicApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    url_id = 'url_id_example' # str | 
    url = 'url_example' # str | 
    page_title = 'page_title_example' # str | 
    subscribed_or_unsubscribed = 'subscribed_or_unsubscribed_example' # str | 
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.update_user_notification_page_subscription_status(tenant_id, url_id, url, page_title, subscribed_or_unsubscribed, sso=sso)
        print("The response of PublicApi->update_user_notification_page_subscription_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->update_user_notification_page_subscription_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **url_id** | **str**|  | 
 **url** | **str**|  | 
 **page_title** | **str**|  | 
 **subscribed_or_unsubscribed** | **str**|  | 
 **sso** | **str**|  | [optional] 

### Return type

[**UpdateUserNotificationStatus200Response**](UpdateUserNotificationStatus200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_notification_status**
> UpdateUserNotificationStatus200Response update_user_notification_status(tenant_id, notification_id, new_status, sso=sso)



### Example


```python
import generated
from generated.models.update_user_notification_status200_response import UpdateUserNotificationStatus200Response
from generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = generated.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = generated.PublicApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    notification_id = 'notification_id_example' # str | 
    new_status = 'new_status_example' # str | 
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.update_user_notification_status(tenant_id, notification_id, new_status, sso=sso)
        print("The response of PublicApi->update_user_notification_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->update_user_notification_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **notification_id** | **str**|  | 
 **new_status** | **str**|  | 
 **sso** | **str**|  | [optional] 

### Return type

[**UpdateUserNotificationStatus200Response**](UpdateUserNotificationStatus200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_image**
> UploadImageResponse upload_image(tenant_id, file, size_preset=size_preset, url_id=url_id)



Upload and resize an image

### Example


```python
import generated
from generated.models.size_preset import SizePreset
from generated.models.upload_image_response import UploadImageResponse
from generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = generated.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = generated.PublicApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    file = None # bytearray | 
    size_preset = generated.SizePreset() # SizePreset | Size preset: \"Default\" (1000x1000px) or \"CrossPlatform\" (creates sizes for popular devices) (optional)
    url_id = 'url_id_example' # str | Page id that upload is happening from, to configure (optional)

    try:
        api_response = api_instance.upload_image(tenant_id, file, size_preset=size_preset, url_id=url_id)
        print("The response of PublicApi->upload_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->upload_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **file** | **bytearray**|  | 
 **size_preset** | [**SizePreset**](.md)| Size preset: \&quot;Default\&quot; (1000x1000px) or \&quot;CrossPlatform\&quot; (creates sizes for popular devices) | [optional] 
 **url_id** | **str**| Page id that upload is happening from, to configure | [optional] 

### Return type

[**UploadImageResponse**](UploadImageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vote_comment**
> VoteComment200Response vote_comment(tenant_id, comment_id, url_id, broadcast_id, vote_body_params, session_id=session_id, sso=sso)



### Example


```python
import generated
from generated.models.vote_body_params import VoteBodyParams
from generated.models.vote_comment200_response import VoteComment200Response
from generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://fastcomments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = generated.Configuration(
    host = "https://fastcomments.com"
)


# Enter a context with an instance of the API client
with generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = generated.PublicApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    comment_id = 'comment_id_example' # str | 
    url_id = 'url_id_example' # str | 
    broadcast_id = 'broadcast_id_example' # str | 
    vote_body_params = generated.VoteBodyParams() # VoteBodyParams | 
    session_id = 'session_id_example' # str |  (optional)
    sso = 'sso_example' # str |  (optional)

    try:
        api_response = api_instance.vote_comment(tenant_id, comment_id, url_id, broadcast_id, vote_body_params, session_id=session_id, sso=sso)
        print("The response of PublicApi->vote_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->vote_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **comment_id** | **str**|  | 
 **url_id** | **str**|  | 
 **broadcast_id** | **str**|  | 
 **vote_body_params** | [**VoteBodyParams**](VoteBodyParams.md)|  | 
 **session_id** | **str**|  | [optional] 
 **sso** | **str**|  | [optional] 

### Return type

[**VoteComment200Response**](VoteComment200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

