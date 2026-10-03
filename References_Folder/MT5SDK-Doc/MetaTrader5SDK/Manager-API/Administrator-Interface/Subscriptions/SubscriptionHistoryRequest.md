[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Subscriptions](../Subscriptions.md) / SubscriptionHistoryRequest

[Previous](SubscriptionHistoryDeleteBatch.md) | [Next](SubscriptionHistoryRequestByID.md)

# IMTAdminAPI::SubscriptionHistoryRequest

Request user subscription action from the server for the specified date range.

C++
    
    
    MTAPIRES  IMTAdminAPI::SubscriptionHistoryRequest(
       const UINT64                  login,    // Login
       const INT64                   from,     // Period start
       const INT64                   to,       // Period end
       IMTSubscriptionHistoryArray*  records   // Array of actions
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.SubscriptionHistoryRequest(
       ulong                         login,    // Login
       long                          from,     // Period start
       long                          to,       // Period end
       CIMTSubscriptionHistoryArray  records   // Array of actions
       )

### Parameters

**login**  
[in] The login of the user whose actions you want to obtain.

**from**  
[in] The beginning of the period for which you need to get actions. The date is specified in seconds since 01.01.1970.

**to**  
[in] The end of the period for which you need to get actions. The date is specified in seconds since 01.01.1970.

**records**  
[out] Object of anarray of subscription actions. The 'records' object must be pre-created by theIMTAdminAPI::SubscriptionHistoryCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method cannot be called from event handlers (any IMT*Sink class methods).
