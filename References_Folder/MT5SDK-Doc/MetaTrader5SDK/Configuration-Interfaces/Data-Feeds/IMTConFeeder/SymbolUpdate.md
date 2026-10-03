[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Data Feeds](../../Data-Feeds.md) / [IMTConFeeder](../IMTConFeeder.md) / SymbolUpdate

[Previous](SymbolAdd.md) | [Next](SymbolShift.md)

# IMTConFeeder::SymbolUpdate

Change [the symbol](../../Symbols.md) with a specified index, for which the data feed transmits quotes.

C++
    
    
    MTAPIRES  IMTConFeeder::SymbolUpdate(
       const UINT  pos,      // Position of the symbol
       LPCWSTR     path      // Path to the symbol
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFeeder.SymbolUpdate(
       uint        pos,      // Position of the symbol
       string      path      // Path to the symbol
       )

Python (Manager API)
    
    
    MTConFeeder.SymbolUpdate(
       pos,        # Position of the symbol
       path        # Path to the symbol
       )

### Parameters

**pos**  
[in] Position of the symbol.

**path**  
[in] Path to a symbol or group of symbols in accordance with the hierarchy of symbols in the trading platform.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
