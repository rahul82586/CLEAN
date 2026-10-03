[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Subscriptions](../Subscriptions.md) / SubscriptionCfgCreate

[Previous](../Subscriptions.md) | [Next](SubscriptionCfgSymbolCreate.md)

# IMTAdminAPI::SubscriptionCfgCreate

Create a subscription configuration object.

C++
    
    
    IMTConSubscription*  IMTAdminAPI::SubscriptionCfgCreate()

.NET
    
    
    CIMTConSubscription  CIMTAdminAPI.SubscriptionCfgCreate()

### Return Value

The function returns a pointer to the created object that implements the [IMTConSubscription](../../../../Configuration-Interfaces/Subscriptions/IMTConSubscription.md) interface. Null is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTConSubscription::Release](../../../../Configuration-Interfaces/Subscriptions/IMTConSubscription/Release.md) method of this object.
