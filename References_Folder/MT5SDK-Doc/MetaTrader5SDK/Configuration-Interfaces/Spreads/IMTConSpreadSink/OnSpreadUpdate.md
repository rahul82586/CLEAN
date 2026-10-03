[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Spreads](../../Spreads.md) / [IMTConSpreadSink](../IMTConSpreadSink.md) / OnSpreadUpdate

[Previous](OnSpreadAdd.md) | [Next](OnSpreadDelete.md)

# IMTConSpreadSink::OnSpreadUpdate

A handler of the event of updating a spread configuration.

C++
    
    
    virtual void  IMTConSpreadSink::OnSpreadUpdate(
       const IMTConSpread*  config      // Pointer to the spread object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConSpreadSink.OnSpreadUpdate(
       CIMTConSpread        config      // Spread object
       )

### Parameters

**config**  
[in] A pointer to the updated spread configuration object.

### Note

This method is called by API to notify that a spread configuration has been changed.
