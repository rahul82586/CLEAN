[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Subscriptions](../Subscriptions.md) / SubscriptionRequestByLogins

[Previous](SubscriptionRequestByGroup.md) | [Next](SubscriptionHistoryCreate.md)

# IMTAdminAPI::SubscriptionRequestByLogins

Request subscriptions from the server by a list of logins.

C++
    
    
    MTAPIRES  IMTAdminAPI::SubscriptionRequestByLogins(
       const UINT64*          logins,       // Logins
       const UINT             logins_total, // Number of logins
       IMTSubscriptionArray*  records       // Object of array of subscriptions
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.SubscriptionRequestByLogins(
       ulong[]                logins,       // Logins
       CIMTSubscriptionArray  records       // Object of array of subscriptions
       )

### Parameters

**logins**  
[in] Array of client logins.

**logins_total**  
[in] Number of logins in the 'logins' array.

**records**  
[out] An object of thearray of subscriptions. The 'records' object must be previously created via theIMTAdminAPI::SubscriptionCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method cannot be called from event handlers (any IMT*Sink class methods).
