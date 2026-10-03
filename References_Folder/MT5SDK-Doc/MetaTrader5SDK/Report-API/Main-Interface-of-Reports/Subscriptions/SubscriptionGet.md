[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Subscriptions](../Subscriptions.md) / SubscriptionGet

[Previous](SubscriptionExist.md) | [Next](SubscriptionGetBySubscription.md)

# IMTReportAPI::SubscriptionGet

Get all subscriptions of a user.
    
    
    MTAPIRES  IMTReportAPI::SubscriptionGet(
       const UINT64           login,    // Login
       IMTSubscriptionArray*  records   // Array of subscriptions
       )

### Parameters

**login**  
[in] The login of the user whose subscriptions you want to obtain.

**records**  
[out] An object of thearray of subscriptions. The 'records' object must be previously created via theIMTServerAPI::SubscriptionCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
