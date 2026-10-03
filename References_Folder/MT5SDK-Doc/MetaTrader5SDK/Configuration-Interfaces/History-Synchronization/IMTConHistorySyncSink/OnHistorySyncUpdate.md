[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [History Synchronization](../../History-Synchronization.md) / [IMTConHistorySyncSink](../IMTConHistorySyncSink.md) / OnHistorySyncUpdate

[Previous](OnHistorySyncAdd.md) | [Next](OnHistorySyncDelete.md)

# IMTConHistorySyncSink::OnHistorySyncUpdate

A handler of the event of update of a configuration of history data synchronization.

C++
    
    
    virtual void  IMTConHistorySyncSink::OnHistorySyncUpdate(
       const IMTConHistorySync*  config      // A pointer to the configuration object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConHistorySyncSink.OnHistorySyncUpdate(
       CIMTConHistorySync        config      // Configuration object
       )

### Parameters

**config**  
[in] A pointer to the object of the updated configuration of data synchronization.

### Note

This method is called by the API to notify that a configuration of data synchronization has been updated.
