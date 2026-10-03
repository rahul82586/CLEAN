[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Subscriptions](../Subscriptions.md) / SubscriptionCfgGet

[Previous](SubscriptionCfgNext.md) | [Next](SubscriptionCfgGetByID.md)

# IMTManagerAPI::SubscriptionCfgGet

Get a subscription configuration by name.

C++
    
    
    MTAPIRES  IMTManagerAPI::SubscriptionCfgGet(
       LPCWSTR              name,     // Configuration name
       IMTConSubscription*  config    // Subscription configuration object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.SubscriptionCfgGet(
       string               name,     // Configuration name
       CIMTConSubscription  config    // Subscription configuration object
       )

### Parameters

**name**  
[in] Configuration name. TheIMTConSubscription::Namevalue is used for the configuration name.

**config**  
[out] Subscription configuration object. The 'config' object must be previously created using theIMTManagerAPI::SubscriptionCfgCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method only works if the [IMTManagerAPI::PUMP_MODE_SUBSCRIPTIONS](../../Connection-to-the-Server/Pumping-Modes.md) pumping mode has been specified during the connection.
