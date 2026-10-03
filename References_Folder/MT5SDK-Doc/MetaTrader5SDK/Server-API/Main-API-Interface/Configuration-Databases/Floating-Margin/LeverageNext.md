[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Floating Margin](../Floating-Margin.md) / LeverageNext

[Previous](LeverageTotal.md) | [Next](LeverageGet.md)

# IMTServerAPI::LeverageNext

Get a floating margin configuration by index.
    
    
    MTAPIRES  IMTServerAPI::LeverageNext(
       const UINT           pos,      // Configuration position
       IMTConLeverage*      config    // Configuration object
       )

### Parameters

**pos**  
[in] Configuration position starting from 0.

**config**  
[out] Configuration object. The config object must be previously created using theIMTServerAPI::LeverageCreatemethod.

### Return Value

An indication of a successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, the code of the encountered error is returned.

### Note

This method copies the subscription configuration with a specified index to the 'config' object.
