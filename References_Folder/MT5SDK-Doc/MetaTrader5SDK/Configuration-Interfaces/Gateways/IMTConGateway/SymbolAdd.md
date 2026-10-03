[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGateway](../IMTConGateway.md) / SymbolAdd

[Previous](ParameterGet.md) | [Next](SymbolUpdate.md)

# IMTConGateway::SymbolAdd

Add [a symbol](../../Symbols.md), for which the gateway will transmit quotes and process trade operations.

C++
    
    
    MTAPIRES  IMTConGateway::SymbolAdd(
       LPCWSTR  path      // Path to the symbol
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGateway.SymbolAdd(
       srting   path      // Path to the symbol
       )

Python (Manager API)
    
    
    MTConGateway.SymbolAdd(
       path     # Path to the symbol
       )

### Parameters

**path**  
[in] Path to a symbol or group of symbols in accordance with the hierarchy of symbols in the trading platform.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

[IMTConSymbol::Path](../../Symbols/IMTConSymbol/Path.md) value is used as the path to the symbol.
