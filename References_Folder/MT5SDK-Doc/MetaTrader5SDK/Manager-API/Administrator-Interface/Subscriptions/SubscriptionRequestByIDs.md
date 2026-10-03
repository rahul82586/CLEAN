[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Subscriptions](../Subscriptions.md) / SubscriptionRequestByIDs

[Previous](SubscriptionRequestByID.md) | [Next](SubscriptionRequestByGroup.md)

# IMTAdminAPI::SubscriptionRequestByIDs

Request subscriptions from the server by a list of IDs.

C++
    
    
    MTAPIRES  IMTAdminAPI::SubscriptionRequestByIDs(
       const UINT64*          ids,       // IDs
       const UINT             ids,       // Number of IDs
       IMTSubscriptionArray*  records    // Object of array of subscriptions
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.SubscriptionRequestByIDs(
       ulong[]                ids,       // IDs
       CIMTSubscriptionArray  records    // Object of array of subscriptions
       )

### Parameters

**ids**  
[in] Array of subscription identifiers. TheIMTSubscription::IDvalue is used as the identifier.

**ids_total**  
[in] The number of identifiers in the 'ids' array.

**records**  
[out] An object of thearray of subscriptions. The 'records' object must be previously created via theIMTAdminAPI::SubscriptionCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method cannot be called from event handlers (any IMT*Sink class methods).
