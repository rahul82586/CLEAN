[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Subscriptions](../Subscriptions.md) / SubscriptionCfgNewsCreate

[Previous](SubscriptionCfgSymbolCreate.md) | [Next](SubscriptionCfgSubscribe.md)

# IMTManagerAPI::SubscriptionCfgNewsCreate

Create a subscription configuration object.

C++
    
    
    IMTConSubscriptionNews*  IMTManagerAPI::SubscriptionCfgNewsCreate()

.NET
    
    
    CIMTConSubscriptionNews  CIMTManagerAPI.SubscriptionCfgNewsCreate()

### Return Value

Returns a pointer to the created object that implements the [IMTConSubscriptionNews](../../../../Configuration-Interfaces/Subscriptions/IMTConSubscriptionNews.md) interface. Null is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTConSubscriptionNews::Release](../../../../Configuration-Interfaces/Subscriptions/IMTConSubscriptionNews/Release.md) method of this object.
