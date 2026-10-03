[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Data Feeds](../../Data-Feeds.md) / [IMTConFeederSink](../IMTConFeederSink.md) / OnFeederUpdate

[Previous](OnFeederAdd.md) | [Next](OnFeederDelete.md)

# IMTConFeederSink::OnFeederUpdate

A handler of the event of updating a data feed configuration.

C++
    
    
    virtual void  IMTConFeederSink::OnFeederUpdate(
       const IMTConFeeder*  feeder      // Pointer to the configuration object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConFeederSink.OnFeederUpdate(
       CIMTConFeeder        feeder      // Configuration object
       )

### Parameters

**feeder**  
[in] A pointer to the updated configuration object.

### Note

This method is called by the API to notify that a data feed configuration has been updated.
