[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Managers](../../Managers.md) / [IMTConManagerSink](../IMTConManagerSink.md) / OnManagerUpdate

[Previous](OnManagerAdd.md) | [Next](OnManagerDelete.md)

# IMTConManagerSink::OnManagerUpdate

A handler of the event of updating manager settings.

C++
    
    
    virtual void  IMTConManagerSink::OnManagerUpdate(
       const IMTConManager*  config      // A pointer to the configuration object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConManagerSink.OnManagerUpdate(
       CIMTConManager        config      // Configuration object
       )

### Parameters

**config**  
[in] A pointer to the updated manager configuration object.

### Note

This method is called by the API to notify that a manager configuration has been updated.
