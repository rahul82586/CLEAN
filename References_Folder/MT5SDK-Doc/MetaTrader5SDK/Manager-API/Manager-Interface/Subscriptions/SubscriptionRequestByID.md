[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Subscriptions](../Subscriptions.md) / SubscriptionRequestByID

[Previous](SubscriptionRequest.md) | [Next](SubscriptionRequestByIDs.md)

# IMTManagerAPI::SubscriptionRequestByID

Request a subscription from the server by ID.

C++
    
    
    MTAPIRES  IMTManagerAPI::SubscriptionRequestByID(
       const UINT64           id,     // ID
       IMTSubscription*       record  // Subscription object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.SubscriptionRequestByID(
       ulong                  id,     // ID
       CIMTSubscription       record  // Subscription object
       )

### Parameters

**id**  
[in] Subscription ID. TheIMTSubscription::IDvalue is used as the identifier.

**record**  
[out]Subscriptionobject. The 'record' object must be previously created via theIMTManagerAPI::SubscriptionCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method cannot be called from event handlers (any IMT*Sink class methods).
