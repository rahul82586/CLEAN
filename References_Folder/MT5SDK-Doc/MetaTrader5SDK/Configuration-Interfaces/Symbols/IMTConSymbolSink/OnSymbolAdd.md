[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbolSink](../IMTConSymbolSink.md) / OnSymbolAdd

[Previous](../IMTConSymbolSink.md) | [Next](OnSymbolUpdate.md)

# IMTConSymbolSink::OnSymbolAdd

A handler of the event of adding a new symbol.

C++
    
    
    virtual void  IMTConSymbolSink::OnSymbolAdd(
       const IMTConSymbol*  config      // A pointer to the symbol object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConSymbolSink.OnSymbolAdd(
       CIMTConSymbol        config      // A symbol object
       )

### Parameters

**config**  
[in] A pointer to the object of the added symbol.

### Note

This method is called by the API to notify that a new symbol has been added.
