[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerSink](../IMTConServerSink.md) / OnConServerUpdate

[Previous](OnConServerAdd.md) | [Next](OnConServerDelete.md)

# IMTConServerSink::OnConServerUpdate

A handler of the event of updating a server configuration.

C++
    
    
    virtual void  IMTConServerSink::OnConServerUpdate(
       const IMTConServer*  server      // Pointer to the configuration object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConServerSink.OnConServerUpdate(
       CIMTConServer        server      // Configuration object
       )

### Parameters

**server**  
[in] A pointer to the updated configuration object.

### Note

This method is called by the API to notify that a server configuration has been updated.
