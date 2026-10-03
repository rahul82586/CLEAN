[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Data Feeds](../../Data-Feeds.md) / [IMTConFeederSink](../IMTConFeederSink.md) / OnFeederAdd

[Previous](../IMTConFeederSink.md) | [Next](OnFeederUpdate.md)

# IMTConFeederSink::OnFeederAdd

A handler of the event of adding a new data feed configuration.

C++
    
    
    virtual void  IMTConFeederSink::OnFeederAdd(
       const IMTConFeeder*  feeder      // Pointer to the configuration object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConFeederSink.OnFeederAdd(
       CIMTConFeeder        feeder      // Configuration object
       )

### Parameters

**feeder**  
[in] A pointer to the object of the added configuration.

### Note

This method is called by the API to notify that a new data feed configuration has been added.
