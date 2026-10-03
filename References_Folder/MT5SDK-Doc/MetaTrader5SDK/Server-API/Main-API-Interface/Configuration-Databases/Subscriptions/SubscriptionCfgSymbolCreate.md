[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Subscriptions](../Subscriptions.md) / SubscriptionCfgSymbolCreate

[Previous](SubscriptionCfgCreate.md) | [Next](SubscriptionCfgNewsCreate.md)

# IMTServerAPI::SubscriptionCfgSymbolCreate

Create a subscription configuration object.
    
    
    IMTConSubscriptionSymbol*  IMTServerAPI::SubscriptionCfgSymbolCreate()

### Return Value

Returns a pointer to the created object that implements the [IMTConSubscriptionSymbol](../../../../Configuration-Interfaces/Subscriptions/IMTConSubscriptionSymbol.md) interface. Null is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTConSubscriptionSymbol::Release](../../../../Configuration-Interfaces/Subscriptions/IMTConSubscriptionSymbol/Release.md) method of this object.
