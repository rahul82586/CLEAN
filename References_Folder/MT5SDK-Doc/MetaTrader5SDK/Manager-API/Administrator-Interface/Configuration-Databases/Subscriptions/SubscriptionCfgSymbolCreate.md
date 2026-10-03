[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Subscriptions](../Subscriptions.md) / SubscriptionCfgSymbolCreate

[Previous](SubscriptionCfgCreate.md) | [Next](SubscriptionCfgNewsCreate.md)

# IMTAdminAPI::SubscriptionCfgSymbolCreate

Create a subscription symbol configuration object.

C++
    
    
    IMTConSubscriptionSymbol*  IMTAdminAPI::SubscriptionCfgSymbolCreate()

.NET
    
    
    CIMTConSubscriptionSymbol  CIMTAdminAPI.SubscriptionCfgSymbolCreate()

### Return Value

Returns a pointer to the created object that implements the [IMTConSubscriptionSymbol](../../../../Configuration-Interfaces/Subscriptions/IMTConSubscriptionSymbol.md) interface. Null is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTConSubscriptionSymbol::Release](../../../../Configuration-Interfaces/Subscriptions/IMTConSubscriptionSymbol/Release.md) method of this object.
