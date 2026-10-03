[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerSink](../IMTConServerSink.md) / OnConServerDelete

[Previous](OnConServerUpdate.md) | [Next](OnConServerSync.md)

# IMTConServerSink::OnConServerDelete

A handler of the event of removing a server configuration.

C++
    
    
    virtual void  IMTConServerSink::OnConServerDelete(
       const IMTConServer*  server      // Pointer to the configuration object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConServerSink.OnConServerDelete(
       CIMTConServer        server      // Configuration object
       )

### Parameters

**server**  
[in] A pointer to the object of the deleted configuration.

### Note

This method is called by the API to notify that a server configuration has been deleted.
