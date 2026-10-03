[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGateway](../IMTConGateway.md) / SymbolClear

[Previous](SymbolDelete.md) | [Next](SymbolTotal.md)

# IMTConGateway::SymbolClear

Clear the list of [symbols](../../Symbols.md) processed by the gateway.

C++
    
    
    MTAPIRES  IMTConGateway::SymbolClear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGateway.SymbolClear()

Python (Manager API)
    
    
    MTConGateway.SymbolClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method clears the entire list of symbols of a data feed.
