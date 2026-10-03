[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Spreads](../../Spreads.md) / [IMTConSpreadSink](../IMTConSpreadSink.md) / OnSpreadAdd

[Previous](../IMTConSpreadSink.md) | [Next](OnSpreadUpdate.md)

# IMTConSpreadSink::OnSpreadAdd

A handler of the event of adding a new spread configuration.

C++
    
    
    virtual void  IMTConSpreadSink::OnSpreadAdd(
       const IMTConSpread*  config      // Pointer to the spread object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConSpreadSink.OnSpreadAdd(
       CIMTConSpread        config      // Spread object
       )

### Parameters

**config**  
[in] A pointer to the object of the added spread configuration.

### Note

This method is called by the API to notify of adding of a new spread configuration.
