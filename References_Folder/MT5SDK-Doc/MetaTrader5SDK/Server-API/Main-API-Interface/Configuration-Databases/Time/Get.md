[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Time](../Time.md) / Get

[Previous](CurrentMsc.md) | [Next](Set.md)

# IMTServerAPI::TimeGet

Get the time configuration.
    
    
    MTAPIRES  IMTServerAPI::TimeGet(
       IMTConTime*  config      // An object of time configuration
       )

### Parameters

**config**  
[out] An object of the time configuration. The config object must first be created using theIMTServerAPI::TimeCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
