[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Common](../Common.md) / Get

[Previous](Unsubscribe.md) | [Next](Set.md)

# IMTServerAPI::CommonGet

Gets the common platform configuration.
    
    
    MTAPIRES  IMTServerAPI::CommonGet(
       IMTConCommon*  common      // An object of configuration
       )

### Parameters

**common**  
[out] An object of the common configuration. The object must first be created using theIMTServerAPI::CommonCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
