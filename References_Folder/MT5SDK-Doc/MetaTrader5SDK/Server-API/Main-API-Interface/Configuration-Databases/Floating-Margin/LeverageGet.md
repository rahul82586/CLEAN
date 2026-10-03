[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Floating Margin](../Floating-Margin.md) / LeverageGet

[Previous](LeverageNext.md) | [Next](../../Clients.md)

# IMTServerAPI::LeverageGet

Get a floating margin configuration by name.
    
    
    MTAPIRES  IMTServerAPI::LeverageGet(
       LPCWSTR              name,     // Configuration name
       IMTConLeverage*      config    // Configuration object
       )

### Parameters

**name**  
[in] Configuration name. TheIMTConSubscription::Namevalue is used for the configuration name.

**config**  
[out] Configuration object. The config object must be previously created using theIMTServerAPI::LeverageCreatemethod.

### Return Value

An indication of a successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, the code of the encountered error is returned.
