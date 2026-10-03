[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Configuration Databases](../../Configuration-Databases.md) / [Subscriptions](../Subscriptions.md) / SubscriptionCfgGet

[Previous](SubscriptionCfgNext.md) | [Next](SubscriptionCfgGetByID.md)

# IMTReportAPI::SubscriptionCfgGet

Get a subscription configuration by name.
    
    
    MTAPIRES  IMTReportAPI::SubscriptionCfgGet(
       LPCWSTR              name,     // Configuration name
       IMTConSubscription*  config    // Subscription configuration object
       )

### Parameters

**name**  
[in] Configuration name. TheIMTConSubscription::Namevalue is used for the configuration name.

**config**  
[out] Subscription configuration object. The 'config' object must first be created using theIMTReportAPI::SubscriptionCfgCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
