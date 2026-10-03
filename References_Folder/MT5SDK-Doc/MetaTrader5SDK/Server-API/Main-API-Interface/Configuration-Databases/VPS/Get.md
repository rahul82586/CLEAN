[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [VPS](../VPS.md) / Get

[Previous](Unsubscribe.md) | [Next](Set.md)

# IMTServerAPI::VPSGet

Get VPS sponsorship settings.
    
    
    MTAPIRES  IMTServerAPI::VPSGet(
       IMTConVPS*  config  // VPS settings object
       )

### Parameters

**config**  
[out] Settings objectIMTConVPS. The 'config' object must be previously created using theIMTServerAPI::MessengerCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
