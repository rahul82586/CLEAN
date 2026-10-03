[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Subscriptions](../Subscriptions.md) / SubscriptionHistoryRequestByIDs

[Previous](SubscriptionHistoryRequestByID.md) | [Next](SubscriptionHistoryRequestByGroup.md)

# IMTAdminAPI::SubscriptionHistoryRequestByIDs

Request subscription actions from the server by a list of identifiers.

C++
    
    
    MTAPIRES  IMTAdminAPI::SubscriptionHistoryRequestByIDs(
       const UINT64*                 ids,       // IDs
       const UINT                    ids,       // Number of IDs
       IMTSubscriptionHistoryArray*  records    // Object of the actions array
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.SubscriptionHistoryRequestByIDs(
       ulong[]                       ids,       // IDs
       CIMTSubscriptionHistoryArray  records    // Object of an array of actions
       )

### Parameters

**ids**  
[in] Array of action identifiers. TheIMTSubscriptionHistory::IDvalue is used for the identifier.

**ids_total**  
[in] The number of identifiers in the 'ids' array.

**records**  
[out] Object of anarray of subscription actions. The 'records' object must be pre-created by theIMTAdminAPI::SubscriptionHistoryCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method cannot be called from event handlers (any IMT*Sink class methods).
