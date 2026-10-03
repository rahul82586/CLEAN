[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Subscriptions](../Subscriptions.md) / SubscriptionGet

[Previous](SubscriptionDelete.md) | [Next](SubscriptionGetBySubscription.md)

# IMTServerAPI::SubscriptionGet

Get all subscriptions of a user.
    
    
    MTAPIRES  IMTServerAPI::SubscriptionGet(
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
