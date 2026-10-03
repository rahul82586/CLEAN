[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Subscriptions](../Subscriptions.md) / SubscriptionUpdate

[Previous](SubscriptionAdd.md) | [Next](SubscriptionDelete.md)

# IMTServerAPI::SubscriptionUpdate

Edit a user subscription in the server database.
    
    
    MTAPIRES  IMTServerAPI::SubscriptionUpdate(
       IMTSubscription*         record        // Subscription description
       )

### Parameters

**record**  
[in]Subscription description. The key field for finding an exiting record isIMTSubscription::ID.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned. For example, if the specified subscription does not exist, the response code [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) will be returned.

### Note

When the method is called, it is NOT checked whether subscription change is allowed according to the [IMTConSubscription::ControlMode](../../../Configuration-Interfaces/Subscriptions/IMTConSubscription/ControlMode.md) parameter. Changes take place directly in the database.
