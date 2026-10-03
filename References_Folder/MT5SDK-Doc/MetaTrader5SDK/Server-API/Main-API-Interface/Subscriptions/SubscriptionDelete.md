[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Subscriptions](../Subscriptions.md) / SubscriptionDelete

[Previous](SubscriptionUpdate.md) | [Next](SubscriptionGet.md)

# IMTServerAPI::SubscriptionDelete

Delete a user subscription from the server database.
    
    
    MTAPIRES  IMTServerAPI::SubscriptionDelete(
       const UINT64  id          // Subscription ID
       )

### Parameters

**id**  
[in] Subscription ID. TheIMTSubscription::IDvalue is used as the identifier.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned. For example, if the specified subscription does not exist, the response code [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) will be returned.

### Note

When the method is called, it is NOT checked whether subscription change is allowed according to the [IMTConSubscription::ControlMode](../../../Configuration-Interfaces/Subscriptions/IMTConSubscription/ControlMode.md) parameter. Changes take place directly in the database.
