[🏠 Document Start](../../../../README.md) / [Gateway API](../../../README.md) / [Main Interface](../../../Main-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Spreads](../Spreads.md) / SpreadGet

[Previous](SpreadNext.md) | [Next](../../Trade-Databases.md)

# IMTGatewayAPI::SpreadGet

Receiving a spread configuration by the identifier.

C++
    
    
    MTAPIRES  IMTGatewayAPI::SpreadGet(
       UINT           id,         // Configuration name
       IMTConSpread*  spread      // Spread configuration object
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.SpreadGet(
       uint           id,         // Configuration name
       CIMTConSpread  spread      // Spread configuration object
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
