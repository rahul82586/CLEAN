[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Subscriptions](../Subscriptions.md) / SubscriptionAdd

[Previous](SubscriptionExist.md) | [Next](SubscriptionUpdate.md)

# IMTServerAPI::SubscriptionAdd

Add a user subscription to the server database.
    
    
    MTAPIRES  IMTServerAPI::SubscriptionAdd(
       IMTSubscription*         record        // Subscription description
       )

### Parameters

**record**  
[in]Subscription description. The key field for finding an exiting record isIMTSubscription::ID.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned. For example, if the specified subscription does not exist, the response code [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) will be returned.

### Note

When the method is called, it is NOT checked whether subscription change is allowed according to the [IMTConSubscription::ControlMode](../../../Configuration-Interfaces/Subscriptions/IMTConSubscription/ControlMode.md) parameter. Changes take place directly in the database. Also, in this case, the subscription cost is not debited from the trader's account.
