[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbolSink](../IMTConSymbolSink.md) / OnSymbolUpdate

[Previous](OnSymbolAdd.md) | [Next](OnSymbolDelete.md)

# IMTConSymbolSink::OnSymbolUpdate

A handler of the event of updating symbol settings.

C++
    
    
    virtual void  IMTConSymbolSink::OnSymbolUpdate(
       const IMTConSymbol*  config      // A pointer to the symbol object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConSymbolSink.OnSymbolUpdate(
       CIMTConSymbol        config      // A symbol object
       )

### Parameters

**config**  
[in] A pointer to the updated symbol object.

### Note

This method is called by the API to notify of change of symbol settings.
