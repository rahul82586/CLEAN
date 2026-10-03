[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Mail Servers](../../Mail-Servers.md) / [IMTConEmailSink](../IMTConEmailSink.md) / OnEmailAdd

[Previous](../IMTConEmailSink.md) | [Next](OnEmailUpdate.md)

# IMTConEmailSink::OnEmailAdd

Handler of the addition of a new mail server configuration.

C++
    
    
    virtual void  IMTConEmailSink::OnEmailAdd(
       const IMTConEmail*  config       // A pointer to the configuration object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConEmailSink.OnEmailAdd(
       CIMTConEmail        config       // Configuration object
       )

### Parameters

**config**  
[in] A pointer to the object of the added configuration.

### Note

This method is called by the API to notify of adding of a new mail server configuration.
