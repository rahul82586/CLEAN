[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Subscriptions](../Subscriptions.md) / SubscriptionHistoryGet

[Previous](SubscriptionHistoryCreateArray.md) | [Next](SubscriptionHistoryGetByID.md)

# IMTReportAPI::SubscriptionHistoryGet

Get user subscription action from the server for the specified date range.
    
    
    MTAPIRES  IMTReportAPI::SubscriptionHistoryGet(
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
[out] Object of anarray of subscription actions. The 'records' object must first be created by theIMTReportAPI::SubscriptionHistoryCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
