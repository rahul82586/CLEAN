[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Subscriptions](../Subscriptions.md) / SubscriptionGetByID

[Previous](SubscriptionGetBySubscription.md) | [Next](SubscriptionGetByLogins.md)

# IMTReportAPI::SubscriptionGetByID

Get a subscription by ID.
    
    
    MTAPIRES  IMTReportAPI::SubscriptionGetByID(
       const UINT64           id,     // ID
       IMTSubscription*       record  // Subscription object
       )

### Parameters

**id**  
[in] Subscription ID. TheIMTSubscription::IDvalue is used as the identifier.

**record**  
[out]Subscriptionobject. The 'record' object must be previously created via theIMTReportAPI::SubscriptionCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
