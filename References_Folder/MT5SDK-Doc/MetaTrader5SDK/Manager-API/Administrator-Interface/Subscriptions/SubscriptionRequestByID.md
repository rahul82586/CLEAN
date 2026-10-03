[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Subscriptions](../Subscriptions.md) / SubscriptionRequestByID

[Previous](SubscriptionRequest.md) | [Next](SubscriptionRequestByIDs.md)

# IMTAdminAPI::SubscriptionRequestByID

Request a subscription from the server by ID.

C++
    
    
    MTAPIRES  IMTAdminAPI::SubscriptionRequestByID(
       const UINT64           id,     // ID
       IMTSubscription*       record  // Subscription object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.SubscriptionRequestByID(
       ulong                  id,     // ID
       CIMTSubscription       record  // Subscription object
       )

### Parameters

**id**  
[in] Subscription ID. TheIMTSubscription::IDvalue is used as the identifier.

**record**  
[out]Subscriptionobject. The 'record' object must be previously created via theIMTAdminAPI::SubscriptionCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method cannot be called from event handlers (any IMT*Sink class methods).
