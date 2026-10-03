[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [VPS](../../VPS.md) / [IMTConVPSSink](../IMTConSink.md) / IMTConSink OnUpdate

[Previous](../IMTConSink.md) | [Next](IMTConSink-OnSync.md)

# IMTConVPSSink::OnVPSUpdate

VPS configuration update event handler.

C++
    
    
    virtual void  IMTConVPSSink::OnVPSUpdate(
       const IMTConVPS*   config  // the pointer to the configuration object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConVPSSink.OnVPSUpdate(
       CIIMTConVPS        config  // configuration object
       )

### Parameters

**config**  
[in] The pointer to the updated configuration object.

### Note

The API calls this method to notify of a change in a VPS configuration.
