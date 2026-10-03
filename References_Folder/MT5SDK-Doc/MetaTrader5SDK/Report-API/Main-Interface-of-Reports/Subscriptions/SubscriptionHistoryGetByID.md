[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Subscriptions](../Subscriptions.md) / SubscriptionHistoryGetByID

[Previous](SubscriptionHistoryGet.md) | [Next](SubscriptionHistoryGetByLogins.md)

# IMTReportAPI::SubscriptionHistoryGetByID

Get a subscription action by ID.
    
    
    MTAPIRES  IMTReportAPI::SubscriptionHistoryGetByID(
       const UINT64              id,     // Identifier
       IMTSubscriptionHistory*   record  // Action object
       )

### Parameters

**id**  
[in] Subscription action identifier. TheIMTSubscriptionHistory::IDvalue is used for the identifier.

**record**  
[out]Subscription actionobject. The 'record' object must be previously created via theIMTReportAPI::SubscriptionHistoryCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method cannot be called from event handlers (any IMT*Sink class methods).
