[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Common](../../Common.md) / [IMTConCommonSink](../IMTConSink.md) / IMTConSink OnUpdate

[Previous](../IMTConSink.md) | [Next](IMTConSink-OnSync.md)

# IMTConCommonSink::OnCommonUpdate

The handler of the event of common configuration update.

C++
    
    
    virtual void  IMTConCommonSink::OnCommonUpdate(
       const IMTConCommon*  config      // Pointer to the configuration object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConCommonSink.OnCommonUpdate(
       CIMTConCommon        config      // Configuration object
       )

### Parameters

**config**  
[in] A pointer to the updated configuration object.

### Note

This method is called by the API to notify that a common configuration has been updated.
