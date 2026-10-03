[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Data Feeds](../../Data-Feeds.md) / [IMTConFeederSink](../IMTConFeederSink.md) / OnFeederDelete

[Previous](OnFeederUpdate.md) | [Next](OnFeederSync.md)

# IMTConFeederSink::OnFeederDelete

A handler of the event of removing a data feed configuration.

C++
    
    
    virtual void  IMTConFeederSink::OnFeederDelete(
       const IMTConFeeder*  feeder      // Pointer to the configuration object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConFeederSink.OnFeederDelete(
       CIMTConFeeder        feeder      // Configuration object
       )

### Parameters

**feeder**  
[in] A pointer to the object of the deleted configuration.

### Note

This method is called by the API to notify that a data feed configuration has been deleted.
