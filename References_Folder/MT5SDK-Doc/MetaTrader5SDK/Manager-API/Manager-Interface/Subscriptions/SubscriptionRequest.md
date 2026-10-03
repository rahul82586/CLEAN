[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Subscriptions](../Subscriptions.md) / SubscriptionRequest

[Previous](SubscriptionDeleteBatch.md) | [Next](SubscriptionRequestByID.md)

# IMTManagerAPI::SubscriptionRequest

Request all user subscriptions from the server.

C++
    
    
    MTAPIRES  IMTManagerAPI::SubscriptionRequest(
       const UINT64           login,    // Login
       IMTSubscriptionArray*  records   // Array of subscriptions
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.SubscriptionRequest(
       ulong                  login,  // Login
       CIMTSubscriptionArray  records   // Array of subscriptions
       )

### Parameters

**login**  
[in] The login of the user whose subscriptions you want to obtain.

**records**  
[out] An object of thearray of subscriptions. The 'records' object must be previously created via theIMTManagerAPI::SubscriptionCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method cannot be called from event handlers (any IMT*Sink class methods).
