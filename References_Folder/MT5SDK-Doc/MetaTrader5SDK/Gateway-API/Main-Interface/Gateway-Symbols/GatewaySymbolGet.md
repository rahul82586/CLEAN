[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Gateway Symbols](../Gateway-Symbols.md) / GatewaySymbolGet

[Previous](GatewaySymbolNext.md) | [Next](../Processing-Trade-Requests.md)

# IMTGatewayAPI::GatewaySymbolDelete

Gets the description of a symbol available to the gateway, by name.

C++
    
    
    MTAPIRES  IMTGatewayAPI::GatewaySymbolDelete(
       LPCWSTR        name,       // Configuration name
       IMTConSymbol*  symbol      // Symbol configuration object
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.GatewaySymbolDelete(
       string         name,       // Configuration name
       CIMTConSymbol  symbol      // Symbol configuration object
       )

### Parameters

**name**  
[in] The name of the configuration.

**symbol**  
[out] An object of the symbol configuration. The symbol object must be previously created using theIMTGatewayAPI::SymbolCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method can only be called from gateways.
