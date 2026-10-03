[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Data Feeds](../../Data-Feeds.md) / [IMTConFeeder](../IMTConFeeder.md) / SymbolNext

[Previous](SymbolTotal.md) | [Next](TranslateAdd.md)

# IMTConFeeder::SymbolNext

Get [a symbol](../../Symbols.md) from the data feed list by the index.

C++
    
    
    LPCWSTR  IMTConFeeder::SymbolNext(
       const UINT  pos      // Position of the symbol
       )  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConFeeder.SymbolNext(
       uint        pos      // Position of the symbol
       )

Python (Manager API)
    
    
    MTConFeeder.SymbolNext(
       pos         # Position of the symbol
       )

### Parameters

**pos**  
[in] Position of a symbol in the list of a data feed, starting with 0.

### Return Value

The path to the symbol in a specified position in the list of symbols for which data are provided by the data feed.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConFeeder](../IMTConFeeder.md) object.
