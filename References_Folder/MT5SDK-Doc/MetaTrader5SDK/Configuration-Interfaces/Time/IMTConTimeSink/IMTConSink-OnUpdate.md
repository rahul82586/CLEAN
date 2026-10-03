[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Time](../../Time.md) / [IMTConTimeSink](../IMTConSink.md) / IMTConSink OnUpdate

[Previous](../IMTConSink.md) | [Next](IMTConSink-OnSync.md)

# IMTConTimeSink::OnTimeUpdate

A handler of the event of update of the platform time settings.

C++
    
    
    virtual void  IMTConTimeSink::OnTimeUpdate(
       const IMTConTime*  config      // An object of the settings
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConTimeSink.OnTimeUpdate(
       CIMTConTime        config      // An object of the settings
       )

### Parameters

**config**  
[in] A pointer to the updated object of settings.

### Note

This method is called by the API to notify of the platform time settings update.
