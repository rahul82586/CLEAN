[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Configuration Databases](../../Configuration-Databases.md) / [Subscriptions](../Subscriptions.md) / SubscriptionCfgNewsCreate

[Previous](SubscriptionCfgSymbolCreate.md) | [Next](SubscriptionCfgTotal.md)

# IMTReportAPI::SubscriptionCfgNewsCreate

Create a subscription configuration object.
    
    
    IMTConSubscriptionNews*  IMTReportAPI::SubscriptionCfgNewsCreate()

### Return Value

Returns a pointer to the created object that implements the [IMTConSubscriptionNews](../../../../Configuration-Interfaces/Subscriptions/IMTConSubscriptionNews.md) interface. Null is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTConSubscriptionNews::Release](../../../../Configuration-Interfaces/Subscriptions/IMTConSubscriptionNews/Release.md) method of this object.
