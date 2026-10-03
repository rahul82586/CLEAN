[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Subscriptions](../Subscriptions.md) / SubscriptionHistoryGet

[Previous](SubscriptionHistoryDelete.md) | [Next](SubscriptionHistoryGetByID.md)

# IMTServerAPI::SubscriptionHistoryGet

Get user subscription action from the server for the specified date range.
    
    
    MTAPIRES  IMTServerAPI::SubscriptionHistoryGet(
       const UINT64                  login,    // Login
       const INT64                   from,     // Period start
       const INT64                   to,       // Period end
       IMTSubscriptionHistoryArray*  records   // Array of actions
       )

### Parameters

**login**  
[in] The login of the user whose actions you want to obtain.

**from**  
[in] The beginning of the period for which you need to get actions. The date is specified in seconds since 01.01.1970.

**to**  
[in] The end of the period for which you need to get actions. The date is specified in seconds since 01.01.1970.

**records**  
[out] Object of anarray of subscription actions. The 'records' object must be pre-created by theIMTServerAPI::SubscriptionHistoryCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
