# Documentation for fastcomments

<a name="documentation-for-api-endpoints"></a>
## Documentation for API Endpoints

All URIs are relative to *https://fastcomments.com*

| Class | Method | HTTP request | Description |
|------------ | ------------- | ------------- | -------------|
| *DefaultApi* | [**addDomainConfig**](Apis/DefaultApi.md#adddomainconfig) | **POST** /api/v1/domain-configs |  |
*DefaultApi* | [**addPage**](Apis/DefaultApi.md#addpage) | **POST** /api/v1/pages |  |
*DefaultApi* | [**addSSOUser**](Apis/DefaultApi.md#addssouser) | **POST** /api/v1/sso-users |  |
*DefaultApi* | [**aggregate**](Apis/DefaultApi.md#aggregate) | **POST** /api/v1/aggregate | Aggregates documents by grouping them (if groupBy is provided) and applying multiple operations. Different operations (e.g. sum, countDistinct, avg, etc.) are supported. |
*DefaultApi* | [**aggregateQuestionResults**](Apis/DefaultApi.md#aggregatequestionresults) | **GET** /api/v1/question-results-aggregation |  |
*DefaultApi* | [**blockUserFromComment**](Apis/DefaultApi.md#blockuserfromcomment) | **POST** /api/v1/comments/{id}/block |  |
*DefaultApi* | [**bulkAggregateQuestionResults**](Apis/DefaultApi.md#bulkaggregatequestionresults) | **POST** /api/v1/question-results-aggregation/bulk |  |
*DefaultApi* | [**combineCommentsWithQuestionResults**](Apis/DefaultApi.md#combinecommentswithquestionresults) | **GET** /api/v1/question-results-aggregation/combine/comments |  |
*DefaultApi* | [**createFeedPost**](Apis/DefaultApi.md#createfeedpost) | **POST** /api/v1/feed-posts |  |
*DefaultApi* | [**createSubscription**](Apis/DefaultApi.md#createsubscription) | **POST** /api/v1/subscriptions |  |
*DefaultApi* | [**createUserBadge**](Apis/DefaultApi.md#createuserbadge) | **POST** /api/v1/user-badges |  |
*DefaultApi* | [**deleteComment**](Apis/DefaultApi.md#deletecomment) | **DELETE** /api/v1/comments/{id} |  |
*DefaultApi* | [**deleteDomainConfig**](Apis/DefaultApi.md#deletedomainconfig) | **DELETE** /api/v1/domain-configs/{domain} |  |
*DefaultApi* | [**deletePage**](Apis/DefaultApi.md#deletepage) | **DELETE** /api/v1/pages/{id} |  |
*DefaultApi* | [**deleteSSOUser**](Apis/DefaultApi.md#deletessouser) | **DELETE** /api/v1/sso-users/{id} |  |
*DefaultApi* | [**deleteSubscription**](Apis/DefaultApi.md#deletesubscription) | **DELETE** /api/v1/subscriptions/{id} |  |
*DefaultApi* | [**deleteUserBadge**](Apis/DefaultApi.md#deleteuserbadge) | **DELETE** /api/v1/user-badges/{id} |  |
*DefaultApi* | [**flagComment**](Apis/DefaultApi.md#flagcomment) | **POST** /api/v1/comments/{id}/flag |  |
*DefaultApi* | [**getAuditLogs**](Apis/DefaultApi.md#getauditlogs) | **GET** /api/v1/audit-logs |  |
*DefaultApi* | [**getComment**](Apis/DefaultApi.md#getcomment) | **GET** /api/v1/comments/{id} |  |
*DefaultApi* | [**getComments**](Apis/DefaultApi.md#getcomments) | **GET** /api/v1/comments |  |
*DefaultApi* | [**getDomainConfig**](Apis/DefaultApi.md#getdomainconfig) | **GET** /api/v1/domain-configs/{domain} |  |
*DefaultApi* | [**getDomainConfigs**](Apis/DefaultApi.md#getdomainconfigs) | **GET** /api/v1/domain-configs |  |
*DefaultApi* | [**getFeedPosts**](Apis/DefaultApi.md#getfeedposts) | **GET** /api/v1/feed-posts |  req tenantId afterId |
*DefaultApi* | [**getPageByURLId**](Apis/DefaultApi.md#getpagebyurlid) | **GET** /api/v1/pages/by-url-id |  |
*DefaultApi* | [**getPages**](Apis/DefaultApi.md#getpages) | **GET** /api/v1/pages |  |
*DefaultApi* | [**getSSOUserByEmail**](Apis/DefaultApi.md#getssouserbyemail) | **GET** /api/v1/sso-users/by-email/{email} |  |
*DefaultApi* | [**getSSOUserById**](Apis/DefaultApi.md#getssouserbyid) | **GET** /api/v1/sso-users/by-id/{id} |  |
*DefaultApi* | [**getSSOUsers**](Apis/DefaultApi.md#getssousers) | **GET** /api/v1/sso-users |  |
*DefaultApi* | [**getSubscriptions**](Apis/DefaultApi.md#getsubscriptions) | **GET** /api/v1/subscriptions |  |
*DefaultApi* | [**getUserBadge**](Apis/DefaultApi.md#getuserbadge) | **GET** /api/v1/user-badges/{id} |  |
*DefaultApi* | [**getUserBadgeProgressById**](Apis/DefaultApi.md#getuserbadgeprogressbyid) | **GET** /api/v1/user-badge-progress/{id} |  |
*DefaultApi* | [**getUserBadgeProgressByUserId**](Apis/DefaultApi.md#getuserbadgeprogressbyuserid) | **GET** /api/v1/user-badge-progress/user/{userId} |  |
*DefaultApi* | [**getUserBadgeProgressList**](Apis/DefaultApi.md#getuserbadgeprogresslist) | **GET** /api/v1/user-badge-progress |  |
*DefaultApi* | [**getUserBadges**](Apis/DefaultApi.md#getuserbadges) | **GET** /api/v1/user-badges |  |
*DefaultApi* | [**patchDomainConfig**](Apis/DefaultApi.md#patchdomainconfig) | **PATCH** /api/v1/domain-configs/{domainToUpdate} |  |
*DefaultApi* | [**patchPage**](Apis/DefaultApi.md#patchpage) | **PATCH** /api/v1/pages/{id} |  |
*DefaultApi* | [**patchSSOUser**](Apis/DefaultApi.md#patchssouser) | **PATCH** /api/v1/sso-users/{id} |  |
*DefaultApi* | [**putDomainConfig**](Apis/DefaultApi.md#putdomainconfig) | **PUT** /api/v1/domain-configs/{domainToUpdate} |  |
*DefaultApi* | [**putSSOUser**](Apis/DefaultApi.md#putssouser) | **PUT** /api/v1/sso-users/{id} |  |
*DefaultApi* | [**saveComment**](Apis/DefaultApi.md#savecomment) | **POST** /api/v1/comments |  |
*DefaultApi* | [**saveCommentsBulk**](Apis/DefaultApi.md#savecommentsbulk) | **POST** /api/v1/comments/bulk |  |
*DefaultApi* | [**unBlockUserFromComment**](Apis/DefaultApi.md#unblockuserfromcomment) | **POST** /api/v1/comments/{id}/un-block |  |
*DefaultApi* | [**unFlagComment**](Apis/DefaultApi.md#unflagcomment) | **POST** /api/v1/comments/{id}/un-flag |  |
*DefaultApi* | [**updateComment**](Apis/DefaultApi.md#updatecomment) | **PATCH** /api/v1/comments/{id} |  |
*DefaultApi* | [**updateFeedPost**](Apis/DefaultApi.md#updatefeedpost) | **PATCH** /api/v1/feed-posts/{id} |  |
*DefaultApi* | [**updateUserBadge**](Apis/DefaultApi.md#updateuserbadge) | **PUT** /api/v1/user-badges/{id} |  |
| *PublicApi* | [**blockFromCommentPublic**](Apis/PublicApi.md#blockfromcommentpublic) | **POST** /block-from-comment/{commentId} |  |
*PublicApi* | [**checkedCommentsForBlocked**](Apis/PublicApi.md#checkedcommentsforblocked) | **GET** /check-blocked-comments |  |
*PublicApi* | [**createCommentPublic**](Apis/PublicApi.md#createcommentpublic) | **POST** /comments/{tenantId} |  |
*PublicApi* | [**createFeedPostPublic**](Apis/PublicApi.md#createfeedpostpublic) | **POST** /feed-posts/{tenantId} |  |
*PublicApi* | [**deleteCommentPublic**](Apis/PublicApi.md#deletecommentpublic) | **DELETE** /comments/{tenantId}/{commentId} |  |
*PublicApi* | [**deleteCommentVote**](Apis/PublicApi.md#deletecommentvote) | **DELETE** /comments/{tenantId}/{commentId}/vote/{voteId} |  |
*PublicApi* | [**deleteFeedPostPublic**](Apis/PublicApi.md#deletefeedpostpublic) | **DELETE** /feed-posts/{tenantId}/{postId} |  |
*PublicApi* | [**flagCommentPublic**](Apis/PublicApi.md#flagcommentpublic) | **POST** /flag-comment/{commentId} |  |
*PublicApi* | [**getCommentText**](Apis/PublicApi.md#getcommenttext) | **GET** /comments/{tenantId}/{commentId}/text |  |
*PublicApi* | [**getCommentVoteUserNames**](Apis/PublicApi.md#getcommentvoteusernames) | **GET** /comments/{tenantId}/{commentId}/votes |  |
*PublicApi* | [**getCommentsPublic**](Apis/PublicApi.md#getcommentspublic) | **GET** /comments/{tenantId} |  req tenantId urlId |
*PublicApi* | [**getEventLog**](Apis/PublicApi.md#geteventlog) | **GET** /event-log/{tenantId} |  req tenantId urlId userIdWS |
*PublicApi* | [**getFeedPostsPublic**](Apis/PublicApi.md#getfeedpostspublic) | **GET** /feed-posts/{tenantId} |  req tenantId afterId |
*PublicApi* | [**getFeedPostsStats**](Apis/PublicApi.md#getfeedpostsstats) | **GET** /feed-posts/{tenantId}/stats |  |
*PublicApi* | [**getGlobalEventLog**](Apis/PublicApi.md#getglobaleventlog) | **GET** /event-log/global/{tenantId} |  req tenantId urlId userIdWS |
*PublicApi* | [**getUserNotificationCount**](Apis/PublicApi.md#getusernotificationcount) | **GET** /user-notifications/get-count |  |
*PublicApi* | [**getUserNotifications**](Apis/PublicApi.md#getusernotifications) | **GET** /user-notifications |  |
*PublicApi* | [**getUserPresenceStatuses**](Apis/PublicApi.md#getuserpresencestatuses) | **GET** /user-presence-status |  |
*PublicApi* | [**getUserReactsPublic**](Apis/PublicApi.md#getuserreactspublic) | **GET** /feed-posts/{tenantId}/user-reacts |  |
*PublicApi* | [**lockComment**](Apis/PublicApi.md#lockcomment) | **POST** /comments/{tenantId}/{commentId}/lock |  |
*PublicApi* | [**pinComment**](Apis/PublicApi.md#pincomment) | **POST** /comments/{tenantId}/{commentId}/pin |  |
*PublicApi* | [**reactFeedPostPublic**](Apis/PublicApi.md#reactfeedpostpublic) | **POST** /feed-posts/{tenantId}/react/{postId} |  |
*PublicApi* | [**resetUserNotificationCount**](Apis/PublicApi.md#resetusernotificationcount) | **POST** /user-notifications/reset-count |  |
*PublicApi* | [**resetUserNotifications**](Apis/PublicApi.md#resetusernotifications) | **POST** /user-notifications/reset |  |
*PublicApi* | [**searchUsers**](Apis/PublicApi.md#searchusers) | **GET** /user-search/{tenantId} |  |
*PublicApi* | [**setCommentText**](Apis/PublicApi.md#setcommenttext) | **POST** /comments/{tenantId}/{commentId}/update-text |  |
*PublicApi* | [**unBlockCommentPublic**](Apis/PublicApi.md#unblockcommentpublic) | **DELETE** /block-from-comment/{commentId} |  |
*PublicApi* | [**unLockComment**](Apis/PublicApi.md#unlockcomment) | **POST** /comments/{tenantId}/{commentId}/unlock |  |
*PublicApi* | [**unPinComment**](Apis/PublicApi.md#unpincomment) | **POST** /comments/{tenantId}/{commentId}/unpin |  |
*PublicApi* | [**updateFeedPostPublic**](Apis/PublicApi.md#updatefeedpostpublic) | **PUT** /feed-posts/{tenantId}/{postId} |  |
*PublicApi* | [**updateUserNotificationCommentSubscriptionStatus**](Apis/PublicApi.md#updateusernotificationcommentsubscriptionstatus) | **POST** /user-notifications/{notificationId}/mark-opted/{optedInOrOut} | Enable or disable notifications for a specific comment. |
*PublicApi* | [**updateUserNotificationPageSubscriptionStatus**](Apis/PublicApi.md#updateusernotificationpagesubscriptionstatus) | **POST** /user-notifications/set-subscription-state/{subscribedOrUnsubscribed} | Enable or disable notifications for a page. When users are subscribed to a page, notifications are created for new root comments, and also |
*PublicApi* | [**updateUserNotificationStatus**](Apis/PublicApi.md#updateusernotificationstatus) | **POST** /user-notifications/{notificationId}/mark/{newStatus} |  |
*PublicApi* | [**uploadImage**](Apis/PublicApi.md#uploadimage) | **POST** /upload-image/{tenantId} | Upload and resize an image |
*PublicApi* | [**voteComment**](Apis/PublicApi.md#votecomment) | **POST** /comments/{tenantId}/{commentId}/vote |  |


<a name="documentation-for-models"></a>
## Documentation for Models

 - [APICreateUserBadgeResponse](./Models/APICreateUserBadgeResponse.md)
 - [APIEmptyResponse](./Models/APIEmptyResponse.md)
 - [APIEmptySuccessResponse](./Models/APIEmptySuccessResponse.md)
 - [APIError](./Models/APIError.md)
 - [APIGetCommentResponse](./Models/APIGetCommentResponse.md)
 - [APIGetCommentsResponse](./Models/APIGetCommentsResponse.md)
 - [APIGetUserBadgeProgressListResponse](./Models/APIGetUserBadgeProgressListResponse.md)
 - [APIGetUserBadgeProgressResponse](./Models/APIGetUserBadgeProgressResponse.md)
 - [APIGetUserBadgeResponse](./Models/APIGetUserBadgeResponse.md)
 - [APIGetUserBadgesResponse](./Models/APIGetUserBadgesResponse.md)
 - [APIPage](./Models/APIPage.md)
 - [APISSOUser](./Models/APISSOUser.md)
 - [APIStatus](./Models/APIStatus.md)
 - [APIUserSubscription](./Models/APIUserSubscription.md)
 - [AddDomainConfigParams](./Models/AddDomainConfigParams.md)
 - [AddDomainConfig_200_response](./Models/AddDomainConfig_200_response.md)
 - [AddDomainConfig_200_response_anyOf](./Models/AddDomainConfig_200_response_anyOf.md)
 - [AddPageAPIResponse](./Models/AddPageAPIResponse.md)
 - [AddSSOUserAPIResponse](./Models/AddSSOUserAPIResponse.md)
 - [AggregateQuestionResultsResponse](./Models/AggregateQuestionResultsResponse.md)
 - [AggregateQuestionResults_200_response](./Models/AggregateQuestionResults_200_response.md)
 - [AggregateTimeBucket](./Models/AggregateTimeBucket.md)
 - [AggregationItem](./Models/AggregationItem.md)
 - [AggregationOpType](./Models/AggregationOpType.md)
 - [AggregationOperation](./Models/AggregationOperation.md)
 - [AggregationRequest](./Models/AggregationRequest.md)
 - [AggregationRequest_sort](./Models/AggregationRequest_sort.md)
 - [AggregationResponse](./Models/AggregationResponse.md)
 - [AggregationResponse_stats](./Models/AggregationResponse_stats.md)
 - [AggregationValue](./Models/AggregationValue.md)
 - [BlockFromCommentParams](./Models/BlockFromCommentParams.md)
 - [BlockFromCommentPublic_200_response](./Models/BlockFromCommentPublic_200_response.md)
 - [BlockSuccess](./Models/BlockSuccess.md)
 - [BulkAggregateQuestionItem](./Models/BulkAggregateQuestionItem.md)
 - [BulkAggregateQuestionResultsRequest](./Models/BulkAggregateQuestionResultsRequest.md)
 - [BulkAggregateQuestionResultsResponse](./Models/BulkAggregateQuestionResultsResponse.md)
 - [BulkAggregateQuestionResults_200_response](./Models/BulkAggregateQuestionResults_200_response.md)
 - [ChangeCommentPinStatusResponse](./Models/ChangeCommentPinStatusResponse.md)
 - [CheckBlockedCommentsResponse](./Models/CheckBlockedCommentsResponse.md)
 - [CheckedCommentsForBlocked_200_response](./Models/CheckedCommentsForBlocked_200_response.md)
 - [CombineCommentsWithQuestionResults_200_response](./Models/CombineCommentsWithQuestionResults_200_response.md)
 - [CombineQuestionResultsWithCommentsResponse](./Models/CombineQuestionResultsWithCommentsResponse.md)
 - [CommentData](./Models/CommentData.md)
 - [CommentHTMLRenderingMode](./Models/CommentHTMLRenderingMode.md)
 - [CommentQuestionResultsRenderingType](./Models/CommentQuestionResultsRenderingType.md)
 - [CommentQuestionsRequired](./Models/CommentQuestionsRequired.md)
 - [CommentTextUpdateRequest](./Models/CommentTextUpdateRequest.md)
 - [CommentThreadDeletionMode](./Models/CommentThreadDeletionMode.md)
 - [CommentUserBadgeInfo](./Models/CommentUserBadgeInfo.md)
 - [CommentUserHashTagInfo](./Models/CommentUserHashTagInfo.md)
 - [CommentUserMentionInfo](./Models/CommentUserMentionInfo.md)
 - [CommenterNameFormats](./Models/CommenterNameFormats.md)
 - [CreateAPIPageData](./Models/CreateAPIPageData.md)
 - [CreateAPISSOUserData](./Models/CreateAPISSOUserData.md)
 - [CreateAPIUserSubscriptionData](./Models/CreateAPIUserSubscriptionData.md)
 - [CreateCommentParams](./Models/CreateCommentParams.md)
 - [CreateCommentPublic_200_response](./Models/CreateCommentPublic_200_response.md)
 - [CreateFeedPostParams](./Models/CreateFeedPostParams.md)
 - [CreateFeedPostPublic_200_response](./Models/CreateFeedPostPublic_200_response.md)
 - [CreateFeedPostResponse](./Models/CreateFeedPostResponse.md)
 - [CreateFeedPost_200_response](./Models/CreateFeedPost_200_response.md)
 - [CreateFeedPostsResponse](./Models/CreateFeedPostsResponse.md)
 - [CreateSubscriptionAPIResponse](./Models/CreateSubscriptionAPIResponse.md)
 - [CreateUserBadgeParams](./Models/CreateUserBadgeParams.md)
 - [CreateUserBadge_200_response](./Models/CreateUserBadge_200_response.md)
 - [CustomConfigParameters](./Models/CustomConfigParameters.md)
 - [DeleteCommentAction](./Models/DeleteCommentAction.md)
 - [DeleteCommentPublic_200_response](./Models/DeleteCommentPublic_200_response.md)
 - [DeleteCommentResult](./Models/DeleteCommentResult.md)
 - [DeleteCommentVote_200_response](./Models/DeleteCommentVote_200_response.md)
 - [DeleteComment_200_response](./Models/DeleteComment_200_response.md)
 - [DeleteDomainConfig_200_response](./Models/DeleteDomainConfig_200_response.md)
 - [DeleteFeedPostPublic_200_response](./Models/DeleteFeedPostPublic_200_response.md)
 - [DeleteFeedPostPublic_200_response_anyOf](./Models/DeleteFeedPostPublic_200_response_anyOf.md)
 - [DeletePageAPIResponse](./Models/DeletePageAPIResponse.md)
 - [DeleteSSOUserAPIResponse](./Models/DeleteSSOUserAPIResponse.md)
 - [DeleteSubscriptionAPIResponse](./Models/DeleteSubscriptionAPIResponse.md)
 - [EventLogEntry](./Models/EventLogEntry.md)
 - [FComment](./Models/FComment.md)
 - [FComment_meta](./Models/FComment_meta.md)
 - [FeedPost](./Models/FeedPost.md)
 - [FeedPostLink](./Models/FeedPostLink.md)
 - [FeedPostMediaItem](./Models/FeedPostMediaItem.md)
 - [FeedPostMediaItemAsset](./Models/FeedPostMediaItemAsset.md)
 - [FeedPostStats](./Models/FeedPostStats.md)
 - [FeedPostsStatsResponse](./Models/FeedPostsStatsResponse.md)
 - [FindCommentsByRangeItem](./Models/FindCommentsByRangeItem.md)
 - [FindCommentsByRangeResponse](./Models/FindCommentsByRangeResponse.md)
 - [FlagCommentPublic_200_response](./Models/FlagCommentPublic_200_response.md)
 - [FlagCommentResponse](./Models/FlagCommentResponse.md)
 - [FlagComment_200_response](./Models/FlagComment_200_response.md)
 - [GetAuditLogsResponse](./Models/GetAuditLogsResponse.md)
 - [GetAuditLogs_200_response](./Models/GetAuditLogs_200_response.md)
 - [GetCommentText_200_response](./Models/GetCommentText_200_response.md)
 - [GetCommentVoteUserNamesSuccessResponse](./Models/GetCommentVoteUserNamesSuccessResponse.md)
 - [GetCommentVoteUserNames_200_response](./Models/GetCommentVoteUserNames_200_response.md)
 - [GetComment_200_response](./Models/GetComment_200_response.md)
 - [GetCommentsPublic_200_response](./Models/GetCommentsPublic_200_response.md)
 - [GetCommentsResponseWithPresence_PublicComment_](./Models/GetCommentsResponseWithPresence_PublicComment_.md)
 - [GetCommentsResponse_PublicComment_](./Models/GetCommentsResponse_PublicComment_.md)
 - [GetComments_200_response](./Models/GetComments_200_response.md)
 - [GetDomainConfig_200_response](./Models/GetDomainConfig_200_response.md)
 - [GetDomainConfigs_200_response](./Models/GetDomainConfigs_200_response.md)
 - [GetDomainConfigs_200_response_anyOf](./Models/GetDomainConfigs_200_response_anyOf.md)
 - [GetDomainConfigs_200_response_anyOf_1](./Models/GetDomainConfigs_200_response_anyOf_1.md)
 - [GetEventLogResponse](./Models/GetEventLogResponse.md)
 - [GetEventLog_200_response](./Models/GetEventLog_200_response.md)
 - [GetFeedPostsPublic_200_response](./Models/GetFeedPostsPublic_200_response.md)
 - [GetFeedPostsResponse](./Models/GetFeedPostsResponse.md)
 - [GetFeedPostsStats_200_response](./Models/GetFeedPostsStats_200_response.md)
 - [GetFeedPosts_200_response](./Models/GetFeedPosts_200_response.md)
 - [GetMyNotificationsResponse](./Models/GetMyNotificationsResponse.md)
 - [GetPageByURLIdAPIResponse](./Models/GetPageByURLIdAPIResponse.md)
 - [GetPagesAPIResponse](./Models/GetPagesAPIResponse.md)
 - [GetPublicFeedPostsResponse](./Models/GetPublicFeedPostsResponse.md)
 - [GetSSOUserByEmailAPIResponse](./Models/GetSSOUserByEmailAPIResponse.md)
 - [GetSSOUserByIdAPIResponse](./Models/GetSSOUserByIdAPIResponse.md)
 - [GetSSOUsers_200_response](./Models/GetSSOUsers_200_response.md)
 - [GetSubscriptionsAPIResponse](./Models/GetSubscriptionsAPIResponse.md)
 - [GetUserBadgeProgressById_200_response](./Models/GetUserBadgeProgressById_200_response.md)
 - [GetUserBadgeProgressList_200_response](./Models/GetUserBadgeProgressList_200_response.md)
 - [GetUserBadge_200_response](./Models/GetUserBadge_200_response.md)
 - [GetUserBadges_200_response](./Models/GetUserBadges_200_response.md)
 - [GetUserNotificationCountResponse](./Models/GetUserNotificationCountResponse.md)
 - [GetUserNotificationCount_200_response](./Models/GetUserNotificationCount_200_response.md)
 - [GetUserNotifications_200_response](./Models/GetUserNotifications_200_response.md)
 - [GetUserPresenceStatusesResponse](./Models/GetUserPresenceStatusesResponse.md)
 - [GetUserPresenceStatuses_200_response](./Models/GetUserPresenceStatuses_200_response.md)
 - [GetUserReactsPublic_200_response](./Models/GetUserReactsPublic_200_response.md)
 - [GifRating](./Models/GifRating.md)
 - [HeaderState](./Models/HeaderState.md)
 - [IgnoredResponse](./Models/IgnoredResponse.md)
 - [ImageContentProfanityLevel](./Models/ImageContentProfanityLevel.md)
 - [ImportedAPIStatus.FAILED](./Models/ImportedAPIStatus.FAILED.md)
 - [ImportedAPIStatus.SUCCESS](./Models/ImportedAPIStatus.SUCCESS.md)
 - [LiveEvent](./Models/LiveEvent.md)
 - [LiveEventType](./Models/LiveEventType.md)
 - [LiveEvent_extraInfo](./Models/LiveEvent_extraInfo.md)
 - [LockComment_200_response](./Models/LockComment_200_response.md)
 - [MediaAsset](./Models/MediaAsset.md)
 - [MetaItem](./Models/MetaItem.md)
 - [NotificationAndCount](./Models/NotificationAndCount.md)
 - [NotificationObjectType](./Models/NotificationObjectType.md)
 - [NotificationType](./Models/NotificationType.md)
 - [PatchDomainConfigParams](./Models/PatchDomainConfigParams.md)
 - [PatchPageAPIResponse](./Models/PatchPageAPIResponse.md)
 - [PatchSSOUserAPIResponse](./Models/PatchSSOUserAPIResponse.md)
 - [Pick_APIComment.UpdatableCommentFields_](./Models/Pick_APIComment.UpdatableCommentFields_.md)
 - [Pick_FComment.APICommentFieldsKeys_](./Models/Pick_FComment.APICommentFieldsKeys_.md)
 - [Pick_FComment.PublicCommentFieldsKeys_](./Models/Pick_FComment.PublicCommentFieldsKeys_.md)
 - [Pick_FComment.approved-or-commentHTML_](./Models/Pick_FComment.approved-or-commentHTML_.md)
 - [Pick_FComment.isDeleted-or-commentHTML-or-commenterName-or-userId_](./Models/Pick_FComment.isDeleted-or-commentHTML-or-commenterName-or-userId_.md)
 - [Pick_FComment_APICommentFieldsKeys__meta](./Models/Pick_FComment_APICommentFieldsKeys__meta.md)
 - [Pick_Omit_FComment.date_.PublicCommentPubSubFieldsKeys_](./Models/Pick_Omit_FComment.date_.PublicCommentPubSubFieldsKeys_.md)
 - [Pick_TenantAuditLog.TenantAuditLogKeys_](./Models/Pick_TenantAuditLog.TenantAuditLogKeys_.md)
 - [PinComment_200_response](./Models/PinComment_200_response.md)
 - [PubSubComment](./Models/PubSubComment.md)
 - [PubSubVote](./Models/PubSubVote.md)
 - [PublicAPIDeleteCommentResponse](./Models/PublicAPIDeleteCommentResponse.md)
 - [PublicAPIGetCommentTextResponse](./Models/PublicAPIGetCommentTextResponse.md)
 - [PublicAPISetCommentTextResponse](./Models/PublicAPISetCommentTextResponse.md)
 - [PublicBlockFromCommentParams](./Models/PublicBlockFromCommentParams.md)
 - [PublicComment](./Models/PublicComment.md)
 - [PublicFeedPostsResponse](./Models/PublicFeedPostsResponse.md)
 - [PutSSOUserAPIResponse](./Models/PutSSOUserAPIResponse.md)
 - [QueryPredicate](./Models/QueryPredicate.md)
 - [QueryPredicate_value](./Models/QueryPredicate_value.md)
 - [QuestionDatum](./Models/QuestionDatum.md)
 - [QuestionRenderingType](./Models/QuestionRenderingType.md)
 - [QuestionResult](./Models/QuestionResult.md)
 - [QuestionResultAggregationOverall](./Models/QuestionResultAggregationOverall.md)
 - [QuestionSubQuestionVisibility](./Models/QuestionSubQuestionVisibility.md)
 - [QuestionWhenSave](./Models/QuestionWhenSave.md)
 - [ReactBodyParams](./Models/ReactBodyParams.md)
 - [ReactFeedPostPublic_200_response](./Models/ReactFeedPostPublic_200_response.md)
 - [ReactFeedPostResponse](./Models/ReactFeedPostResponse.md)
 - [Record_string__before_string_or_null__after_string_or_null___value](./Models/Record_string__before_string_or_null__after_string_or_null___value.md)
 - [Record_string_string_or_number__value](./Models/Record_string_string_or_number__value.md)
 - [RenderableUserNotification](./Models/RenderableUserNotification.md)
 - [ResetUserNotificationsResponse](./Models/ResetUserNotificationsResponse.md)
 - [ResetUserNotifications_200_response](./Models/ResetUserNotifications_200_response.md)
 - [SORT_DIR](./Models/SORT_DIR.md)
 - [SSOSecurityLevel](./Models/SSOSecurityLevel.md)
 - [SaveCommentResponse](./Models/SaveCommentResponse.md)
 - [SaveCommentResponseOptimized](./Models/SaveCommentResponseOptimized.md)
 - [SaveComment_200_response](./Models/SaveComment_200_response.md)
 - [SaveCommentsResponseWithPresence](./Models/SaveCommentsResponseWithPresence.md)
 - [SearchUsersResponse](./Models/SearchUsersResponse.md)
 - [SearchUsers_200_response](./Models/SearchUsers_200_response.md)
 - [SetCommentText_200_response](./Models/SetCommentText_200_response.md)
 - [SizePreset](./Models/SizePreset.md)
 - [SortDirections](./Models/SortDirections.md)
 - [SpamRule](./Models/SpamRule.md)
 - [UnBlockCommentPublic_200_response](./Models/UnBlockCommentPublic_200_response.md)
 - [UnBlockFromCommentParams](./Models/UnBlockFromCommentParams.md)
 - [UnblockSuccess](./Models/UnblockSuccess.md)
 - [UpdateAPIPageData](./Models/UpdateAPIPageData.md)
 - [UpdateAPISSOUserData](./Models/UpdateAPISSOUserData.md)
 - [UpdateDomainConfigParams](./Models/UpdateDomainConfigParams.md)
 - [UpdateFeedPostParams](./Models/UpdateFeedPostParams.md)
 - [UpdateUserBadgeParams](./Models/UpdateUserBadgeParams.md)
 - [UpdateUserBadge_200_response](./Models/UpdateUserBadge_200_response.md)
 - [UpdateUserNotificationStatus_200_response](./Models/UpdateUserNotificationStatus_200_response.md)
 - [UploadImageResponse](./Models/UploadImageResponse.md)
 - [UserBadge](./Models/UserBadge.md)
 - [UserBadgeProgress](./Models/UserBadgeProgress.md)
 - [UserNotification](./Models/UserNotification.md)
 - [UserNotificationWriteResponse](./Models/UserNotificationWriteResponse.md)
 - [UserPresenceData](./Models/UserPresenceData.md)
 - [UserReactsResponse](./Models/UserReactsResponse.md)
 - [UserSearchResult](./Models/UserSearchResult.md)
 - [UserSessionInfo](./Models/UserSessionInfo.md)
 - [VoteBodyParams](./Models/VoteBodyParams.md)
 - [VoteComment_200_response](./Models/VoteComment_200_response.md)
 - [VoteDeleteResponse](./Models/VoteDeleteResponse.md)
 - [VoteDeleteResponse_status](./Models/VoteDeleteResponse_status.md)
 - [VoteResponse](./Models/VoteResponse.md)
 - [VoteResponseUser](./Models/VoteResponseUser.md)
 - [VoteResponse_status](./Models/VoteResponse_status.md)
 - [VoteStyle](./Models/VoteStyle.md)


<a name="documentation-for-authorization"></a>
## Documentation for Authorization

<a name="api_key"></a>
### api_key

- **Type**: API key
- **API key parameter name**: x-api-key
- **Location**: HTTP header

