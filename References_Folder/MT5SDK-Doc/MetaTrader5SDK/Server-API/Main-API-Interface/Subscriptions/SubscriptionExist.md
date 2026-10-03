[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Subscriptions](../Subscriptions.md) / SubscriptionExist

[Previous](SubscriptionCancel.md) | [Next](SubscriptionAdd.md)

# IMTServerAPI::SubscriptionExist

Check if a user has the subscription.
    
    
    bool  IMTServerAPI::SubscriptionExist(
       const UINT64           login,         // Login
       const UINT64           subscription   // Subscription
       )

### Parameters

**login**  
[in] The login of the user whose subscriptions you want to obtain.

**subscription**  
[in] Subscription configuration ID. TheIMTConSubscription::IDvalue is used for the identifier.

### Return Value

Returns TRUE if the subscription exists, otherwise returns FALSE.
