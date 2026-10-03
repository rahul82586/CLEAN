[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGateway](../IMTConGateway.md) / SymbolDelete

[Previous](SymbolShift.md) | [Next](SymbolClear.md)

# IMTConGateway::SymbolDelete

Delete [a symbol](../../Symbols.md) from the list of symbols processed by the gateway by the index.

C++
    
    
    MTAPIRES  IMTConGateway::SymbolDelete(
       const UINT  pos      // Position of the symbol
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGateway.SymbolDelete(
       uint        pos      // Position of the symbol
       )

Python (Manager API)
    
    
    MTConGateway.SymbolDelete(
       pos         # Position of the symbol
       )

### Parameters

**pos**  
[in] Position of the symbol, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) is returned.
