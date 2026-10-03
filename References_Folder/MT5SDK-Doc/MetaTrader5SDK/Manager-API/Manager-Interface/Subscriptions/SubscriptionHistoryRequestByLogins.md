[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Subscriptions](../Subscriptions.md) / SubscriptionHistoryRequestByLogins

[Previous](SubscriptionHistoryRequestByGroup.md) | [Next](../Custom-Functions.md)

# IMTManagerAPI::SubscriptionHistoryRequestByLogins

Request subscription actions from the server by a list of logins.

C++
    
    
    MTAPIRES  IMTManagerAPI::SubscriptionHistoryRequestByLogins(
       const UINT64*                 logins,       // Logins
       const UINT                    logins_total, // Number of logins
       const INT64                   from,         // Period start
       const INT64                   to,           // Period end
       IMTSubscriptionHistoryArray*  records       // Action array object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.SubscriptionHistoryRequestByLogins(
       ulong[]                       logins,       // Logins
       long                          from,         // Period start
       long                          to,           // Period end
       CIMTSubscriptionHistoryArray  records       // Action array object
       )

### Parameters

**logins**  
[in] Array of client logins.

**logins_total**  
[in] Number of logins in the 'logins' array.

**from**  
[in] The beginning of the period for which you need to get actions. The date is specified in seconds since 01.01.1970.

**to**  
[in] The end of the period for which you need to get actions. The date is specified in seconds since 01.01.1970.

**records**  
[out] Object of anarray of subscription actions. The 'records' object must be pre-created by theIMTManagerAPI::SubscriptionHistoryCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method cannot be called from event handlers (any IMT*Sink class methods).
