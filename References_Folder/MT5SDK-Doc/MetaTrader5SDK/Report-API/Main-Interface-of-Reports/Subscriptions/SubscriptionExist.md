[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Subscriptions](../Subscriptions.md) / SubscriptionExist

[Previous](SubscriptionCreateArray.md) | [Next](SubscriptionGet.md)

# IMTReportAPI::SubscriptionExist

Check if a user has the subscription.
    
    
    bool  IMTReportAPI::SubscriptionExist(
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
