[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Spreads](../Spreads.md) / SpreadGet

[Previous](SpreadNext.md) | [Next](../Groups.md)

# IMTServerAPI::SpreadGet

Receiving a spread configuration by the identifier.
    
    
    MTAPIRES  IMTServerAPI::SpreadGet(
       UINT           id,         // Configuration name
       IMTConSpread*  spread      // Spread configuration object
       )

### Parameters

**id**  
[in]Configuration identifier.

**spread**  
[out] Spread configuration object. The spread object must be first created usingIMTServerAPI::SpreadCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

[IMTConSpread::ID](../../../../Configuration-Interfaces/Spreads/IMTConSpread/ID.md) value is used as the identifier.
