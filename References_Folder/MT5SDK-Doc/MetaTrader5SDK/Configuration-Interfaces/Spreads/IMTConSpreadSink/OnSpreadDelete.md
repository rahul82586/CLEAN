[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Spreads](../../Spreads.md) / [IMTConSpreadSink](../IMTConSpreadSink.md) / OnSpreadDelete

[Previous](OnSpreadUpdate.md) | [Next](OnSpreadSync.md)

# IMTConSpreadSink::OnSpreadDelete

A handler of the event of removing a configuration.

C++
    
    
    virtual void  IMTConSpreadSink::OnSpreadDelete(
       const IMTConSymbol*  config      // Pointer to the spread object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConSpreadSink.OnSpreadDelete(
       CIMTConSymbol        config      // Spread object
       )

### Parameters

**config**  
[in] A pointer to the object of the deleted spread configuration.

### Note

This method is called by the API to notify that a spread configuration has been deleted.
