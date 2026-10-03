[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Subscriptions](../Subscriptions.md) / SubscriptionHistoryRequestByID

[Previous](SubscriptionHistoryRequest.md) | [Next](SubscriptionHistoryRequestByIDs.md)

# IMTAdminAPI::SubscriptionHistoryRequestByID

Request a subscription action from the server by its identifier.

C++
    
    
    MTAPIRES  IMTAdminAPI::SubscriptionHistoryRequestByID(
       const UINT64              id,     // Identifier
       IMTSubscriptionHistory*   record  // Action object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.SubscriptionHistoryRequestByID(
       ulong                     id,     // Identifier
       CIMTSubscriptionHistory   record  // Action object
       )

### Parameters

**id**  
[in] Subscription action identifier. TheIMTSubscriptionHistory::IDvalue is used for the identifier.

**record**  
[out]Subscription actionobject. The 'record' object must be previously created via theIMTAdminAPI::SubscriptionHistoryCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method cannot be called from event handlers (any IMT*Sink class methods).
