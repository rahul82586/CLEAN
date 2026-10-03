[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Data Feeds](../../Data-Feeds.md) / [IMTConFeeder](../IMTConFeeder.md) / SymbolClear

[Previous](SymbolDelete.md) | [Next](SymbolTotal.md)

# IMTConFeeder::SymbolClear

Clear the list of [symbols](../../Symbols.md) of the data feed.

C++
    
    
    MTAPIRES  IMTConFeeder::SymbolClear()  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFeeder.SymbolClear()

Python (Manager API)
    
    
    MTConFeeder.SymbolClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method clears the entire list of symbols of a data feed.
