[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGateway](../IMTConGateway.md) / SymbolShift

[Previous](SymbolUpdate.md) | [Next](SymbolDelete.md)

# IMTConGateway::SymbolShift

Change the position of [a symbol](../../Symbols.md) in the list of symbols, for which the gateway transmits quotes and processes trade operations.

C++
    
    
    MTAPIRES  IMTConGateway::SymbolShift(
       const UINT  pos,       // Position of the symbol
       const int   shift      // Shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGateway.SymbolShift(
       uint        pos,       // Position of the symbol
       int         shift      // Shift
       )

Python (Manager API)
    
    
    MTConGateway.SymbolShift(
       pos,        # Position of the symbol
       shift       # Shift
       )

### Parameters

**pos**  
[in] Position of the symbol, starting with 0.

**shift**  
[in] Shift from its current position. A negative value means the shift to the top of the list, a positive value - to its end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
