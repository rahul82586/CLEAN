[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Subscriptions](../Subscriptions.md) / SubscriptionCfgGetByID

[Previous](SubscriptionCfgGet.md) | [Next](SubscriptionCfgRequest.md)

# IMTManagerAPI::SubscriptionCfgGetByID

Get a subscription configuration by ID.

C++
    
    
    MTAPIRES  IMTManagerAPI::SubscriptionCfgGetByID(
       LPCWSTR              name,     // Configuration name
       IMTConSubscription*  config    // Subscription configuration object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.SubscriptionCfgGetByID(
       string               name,     // Configuration name
       CIMTConSubscription  config    // Subscription configuration object
       )

### Parameters

**id**  
[in] Configuration ID. TheIMTConSubscription::IDvalue is used for the identifier.

**config**  
[out] Subscription configuration object. The 'config' object must be previously created using theIMTManagerAPI::SubscriptionCfgCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method only works if the [IMTManagerAPI::PUMP_MODE_SUBSCRIPTIONS](../../Connection-to-the-Server/Pumping-Modes.md) pumping mode has been specified during the connection.
