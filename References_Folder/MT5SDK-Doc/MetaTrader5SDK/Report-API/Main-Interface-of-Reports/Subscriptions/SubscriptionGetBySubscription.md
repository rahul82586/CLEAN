[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Subscriptions](../Subscriptions.md) / SubscriptionGetBySubscription

[Previous](SubscriptionGet.md) | [Next](SubscriptionGetByID.md)

# IMTReportAPI::SubscriptionGetBySubscription

Get a user subscription by the subscription configuration ID.
    
    
    MTAPIRES  IMTReportAPI::SubscriptionGetBySubscription(
       const UINT64           login,         // Login
       const UINT64           subscription   // Subscription
       IMTSubscription*       record         // Subscription object
       )

### Parameters

**login**  
[in] The login of the user whose subscriptions you want to obtain.

**subscription**  
[in] Subscription configuration ID. TheIMTConSubscription::IDvalue is used for the identifier.

**record**  
[out]Subscriptionobject. The 'record' object must be previously created via theIMTReportAPI::SubscriptionCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
