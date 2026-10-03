[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Data Feeds](../../Data-Feeds.md) / [IMTConFeeder](../IMTConFeeder.md) / SymbolAdd

[Previous](ParameterGet.md) | [Next](SymbolUpdate.md)

# IMTConFeeder::SymbolAdd

Add a [symbol](../../Symbols.md), for which the data feed will transmit quotes.

C++
    
    
    MTAPIRES  IMTConFeeder::SymbolAdd(
       LPCWSTR  path      // Path to the symbol
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFeeder.SymbolAdd(
       string   path      // Path to the symbol
       )

Python (Manager API)
    
    
    MTConFeeder.SymbolAdd(
       path     # Path to the symbol
       )

### Parameters

**path**  
[in] Path to a symbol or group of symbols in accordance with the hierarchy of symbols in the trading platform.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
