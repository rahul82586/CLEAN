[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Gateway Symbols](../Gateway-Symbols.md) / GatewaySymbolAdd

[Previous](../Gateway-Symbols.md) | [Next](GatewaySymbolDelete.md)

# IMTGatewayAPI::GatewaySymbolAdd

Adds a new symbol to the list of symbols available to the gateway.

C++
    
    
    MTAPIRES  IMTGatewayAPI::GatewaySymbolAdd(
       IMTConSymbol*  symbol      // Symbol configuration object
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.GatewaySymbolAdd(
       CIMTConSymbol  symbol      // Symbol configuration object
       )

### Parameters

**symbol**  
[in] An object of the symbol configuration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method can only be called from gateways.
