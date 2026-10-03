[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerSink](../IMTConServerSink.md) / OnConServerAdd

[Previous](../IMTConServerSink.md) | [Next](OnConServerUpdate.md)

# IMTConServerSink::OnConServerAdd

A handler of the event of adding a new server configuration.

C++
    
    
    virtual void  IMTConServerSink::OnConServerAdd(
       const IMTConServer*  server      // Pointer to the configuration object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConServerSink.OnConServerAdd(
       CIMTConServer        server      // Configuration object
       )

### Parameters

**server**  
[in] A pointer to the object of the added configuration.

### Note

This method is called by tServer API to notify that a new server configuration has been added.
