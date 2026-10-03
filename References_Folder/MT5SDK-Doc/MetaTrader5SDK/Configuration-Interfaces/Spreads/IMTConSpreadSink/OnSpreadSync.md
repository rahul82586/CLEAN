[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Spreads](../../Spreads.md) / [IMTConSpreadSink](../IMTConSpreadSink.md) / OnSpreadSync

[Previous](OnSpreadDelete.md) | [Next](../../Groups.md)

# IMTConSpreadSink::OnSpreadSync

A handler of the event of synchronization of spread configurations.

C++
    
    
    virtual void  IMTConSpreadSink::OnSpreadSync()

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConSpreadSink.OnSpreadSync()

### Note

This method is called by the API to notify of synchronization of spread configurations.

Synchronization of spread settings is performed on Access, History, Trade and Backup servers during connection to the main server.
