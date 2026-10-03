[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [History Synchronization](../../History-Synchronization.md) / [IMTConHistorySyncSink](../IMTConHistorySyncSink.md) / OnHistorySyncSync

[Previous](OnHistorySyncDelete.md) | [Next](../../Gateways.md)

# IMTConHistorySyncSink::OnHistorySyncSync

A handler of the event of synchronization of configurations of history data synchronization.

C++
    
    
    virtual void  IMTConHistorySyncSink::OnHistorySyncSync()

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConHistorySyncSink.OnHistorySyncSync()

### Note

This method is called by API to notify that history data sync configurations have been synchronized.
