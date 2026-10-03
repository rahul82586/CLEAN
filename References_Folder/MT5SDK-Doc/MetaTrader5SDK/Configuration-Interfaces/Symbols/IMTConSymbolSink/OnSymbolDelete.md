[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbolSink](../IMTConSymbolSink.md) / OnSymbolDelete

[Previous](OnSymbolUpdate.md) | [Next](OnSymbolSync.md)

# IMTConSymbolSink::OnSymbolDelete

A handler of the event of symbol removal.

C++
    
    
    virtual void  IMTConSymbolSink::OnSymbolDelete(
       const IMTConSymbol*  config      // A pointer to the symbol object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConSymbolSink.OnSymbolDelete(
       CIMTConSymbol        config      // A symbol object
       )

### Parameters

**config**  
[in] A pointer to the object of the deleted symbol.

### Note

This method is called by the API to notify of a fact that a symbol has been deleted.
