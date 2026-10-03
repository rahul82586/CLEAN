[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Gateway Symbols](../Gateway-Symbols.md) / GatewaySymbolNext

[Previous](GatewaySymbolTotal.md) | [Next](GatewaySymbolGet.md)

# IMTGatewayAPI::GatewaySymbolDelete

Gets the description of a symbol available to the gateway, by index.

C++
    
    
    MTAPIRES  IMTGatewayAPI::GatewaySymbolDelete(
       const UINT     pos,        // Configuration position
       IMTConSymbol*  symbol      // Symbol configuration object
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.GatewaySymbolDelete(
       uint           pos,        // Configuration position
       CIMTConSymbol  symbol      // Symbol configuration object
       )

### Parameters

**pos**  
[in] Position of the configuration, starting with 0.

**symbol**  
[out] An object of the symbol configuration. The symbol object must be previously created using theIMTGatewayAPI::SymbolCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method can only be called from gateways.
