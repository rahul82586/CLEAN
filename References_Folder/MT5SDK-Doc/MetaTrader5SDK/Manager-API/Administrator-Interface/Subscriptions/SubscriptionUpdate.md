[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Subscriptions](../Subscriptions.md) / SubscriptionUpdate

[Previous](SubscriptionCancelBatch.md) | [Next](SubscriptionUpdateBatch.md)

# IMTAdminAPI::SubscriptionUpdate

Edit a user subscription in the server database.

C++
    
    
    MTAPIRES  IMTAdminAPI::SubscriptionUpdate(
       IMTSubscription*         record        // Subscription description
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTAdminAPI.SubscriptionUpdate(
       CIMTSubscription         record        // Subscription description
       )

### Parameters

**record**  
[in]Subscription description. The key field for finding an exiting record isIMTSubscription::ID.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned. For example, if the specified subscription does not exist, the response code [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) will be returned.

### Note

When the method is called, it is NOT checked whether subscription change is allowed according to the [IMTConSubscription::ControlMode](../../../Configuration-Interfaces/Subscriptions/IMTConSubscription/ControlMode.md) parameter. Changes take place directly in the database.
