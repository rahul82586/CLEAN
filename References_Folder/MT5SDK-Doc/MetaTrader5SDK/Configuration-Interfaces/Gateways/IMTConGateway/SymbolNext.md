[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGateway](../IMTConGateway.md) / SymbolNext

[Previous](SymbolTotal.md) | [Next](GroupAdd.md)

# IMTConGateway::SymbolNext

Get [a symbol](../../Symbols.md) from the list of symbols processed by the gateway by the index.

C++
    
    
    LPCWSTR  IMTConGateway::SymbolNext(
       const UINT  pos      // Position of the symbol
       )  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConGateway.SymbolNext(
       uint        pos      // Position of the symbol
       )

Python (Manager API)
    
    
    MTConGateway.SymbolNext(
       pos         # Position of the symbol
       )

### Parameters

**pos**  
[in] Position of the symbol in the list, starting with 0.

### Return Value

If successful, it returns a pointer to the path to the symbol at the specified position. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConGateway](../IMTConGateway.md) object.
