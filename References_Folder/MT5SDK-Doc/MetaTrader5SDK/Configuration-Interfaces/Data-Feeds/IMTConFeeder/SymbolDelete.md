[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Data Feeds](../../Data-Feeds.md) / [IMTConFeeder](../IMTConFeeder.md) / SymbolDelete

[Previous](SymbolShift.md) | [Next](SymbolClear.md)

# IMTConFeeder::SymbolDelete

Remove [a symbol](../../Symbols.md) from the data feed list by the index.

C++
    
    
    MTAPIRES  IMTConFeeder::SymbolDelete(
       const UINT  pos      // Position of the symbol
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFeeder.SymbolDelete(
       uint        pos      // Position of the symbol
       )

Python (Manager API)
    
    
    MTConFeeder.SymbolDelete(
       pos         # Position of the symbol
       )

### Parameters

**pos**  
[in] Position of the symbol, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) is returned.
