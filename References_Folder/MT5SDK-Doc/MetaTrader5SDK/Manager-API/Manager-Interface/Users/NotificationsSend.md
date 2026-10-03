[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Users](../Users.md) / NotificationsSend

[Previous](UserBalanceCheckBatch.md) | [Next](EmailSend.md)

# IMTManagerAPI::NotificationsSend

Sends push-notifications to a list of MetaQuotes IDs.

C++
    
    
    MTAPIRES  IMTManagerAPI::NotificationsSend(
       LPCWSTR      metaquotest_ids,  // The list of MetaQuotes IDs
       LPCWSTR      message           // Message
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.NotificationsSend(
       string       metaquotest_ids,  // The list of MetaQuotes IDs
       string       message           // Message
       )

Python
    
    
    ManagerAPI.NotificationsSend(
       metaquotest_ids, # The list of MetaQuotes IDs
       message          # Message
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

# IMTManagerAPI::NotificationsSend

Sends push-notifications to a list of logins.

C++
    
    
    MTAPIRES  IMTManagerAPI::NotificationsSend(
       const UINT64* logins,           // Logins
       const UNIT    logins_total,     // Number of logins
       LPCWSTR       message           // Message
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.NotificationsSend(
       ulong[]       logins,           // Logins
       string        message           // Message
       )

Python
    
    
    ManagerAPI.NotificationsSend(
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
