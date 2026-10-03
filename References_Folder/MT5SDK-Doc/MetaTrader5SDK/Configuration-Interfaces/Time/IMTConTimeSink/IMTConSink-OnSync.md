[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Time](../../Time.md) / [IMTConTimeSink](../IMTConSink.md) / IMTConSink OnSync

[Previous](IMTConSink-OnUpdate.md) | [Next](../../Holidays.md)

# IMTConTimeSink::OnTimeSync

A handler of the event of synchronization of the platform time settings.

C++
    
    
    virtual void  IMTConTimeSink::OnTimeSync()

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConTimeSink.OnTimeSync()

### Note

This method is called by the API to notify of the platform time settings synchronization.
