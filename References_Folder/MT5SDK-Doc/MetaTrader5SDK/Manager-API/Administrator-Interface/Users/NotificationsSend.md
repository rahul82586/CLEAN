[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Users](../Users.md) / NotificationsSend

[Previous](UserLogins.md) | [Next](../Trade-Databases.md)

# IMTAdminAPI::NotificationsSend

Sends push-notifications to a list of MetaQuotes IDs.

C++
    
    
    MTAPIRES  IMTAdminAPI::NotificationsSend(
       LPCWSTR      metaquotest_ids,  // The list of MetaQuotes IDs
       LPCWSTR      message           // Message
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.NotificationsSend(
       string       metaquotest_ids,  // The list of MetaQuotes IDs
       srting       message           // Message
       )

Python
    
    
    AdminAPI.NotificationsSend(
       metaquotest_ids,  # The list of MetaQuotes IDs
       message           # Message
       )

### Parameters

**metaquotes_ids**  
[in] A comma separated list of MetaQuotes IDs.

**message**  
[in] The text of the notification.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Push notifications are personal messages sent over the Internet. They do not depend on the phone number or mobile network operator. Messages are delivered instantly; no need to run any applications on the receiver's device.

# IMTAdminAPI::NotificationsSend

Sends push-notifications to a list of logins.

C++
    
    
    MTAPIRES  IMTAdminAPI::NotificationsSend(
       const UINT64* logins,           // Logins
       const UNIT    logins_total,     // Number of logins
       LPCWSTR       message           // Message
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.NotificationsSend(
       ulong[]       logins,           // Logins
       string        message           // Message
       )

Python
    
    
    AdminAPI.NotificationsSend(
       logins,       # Logins
       message       # Message
       )

### Parameters

**logins**  
[in] An array of logins.

**logins_total**  
[in] The total number of logins in logins.

**message**  
[in] The text of the notification.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Push notifications are personal messages sent over the Internet. They do not depend on the phone number or mobile network operator. Messages are delivered instantly; no need to run any applications on the receiver's device.
