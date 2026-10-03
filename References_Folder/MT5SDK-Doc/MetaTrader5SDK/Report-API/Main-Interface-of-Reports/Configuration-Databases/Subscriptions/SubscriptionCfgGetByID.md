[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Configuration Databases](../../Configuration-Databases.md) / [Subscriptions](../Subscriptions.md) / SubscriptionCfgGetByID

[Previous](SubscriptionCfgGet.md) | [Next](../Funds-and-ETF.md)

# IMTReportAPI::SubscriptionCfgGetByID

Get a subscription configuration by ID.
    
    
    MTAPIRES  IMTReportAPI::SubscriptionCfgGetByID(
       const UINT64         id,       // Configuration ID
       IMTConSubscription*  config    // Subscription configuration object
       )

### Parameters

**id**  
[in] Configuration ID. TheIMTConSubscription::IDvalue is used for the identifier.

**config**  
[out] Subscription configuration object. The 'config' object must first be created using theIMTReportAPI::SubscriptionCfgCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
