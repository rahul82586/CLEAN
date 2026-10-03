[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Mail Servers](../../Mail-Servers.md) / [IMTConEmailSink](../IMTConEmailSink.md) / OnEmailDelete

[Previous](OnEmailUpdate.md) | [Next](OnEmailSync.md)

# OnEmailDelete

Handler of the deletion of a mail server configuration.

C++
    
    
    virtual void  IMTConEmailSink::OnEmailDelete(
       const IMTConEmail*   config      // A pointer to the configuration object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConEmailSink.OnEmailDelete(
       CIMTConEmail         config      // Configuration object
       )

### Parameters

**config**  
A pointer to the object of the deleted configuration.

### Note

This method is called by the API to notify of deletion of a mail server configuration.
