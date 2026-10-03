[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Managers](../../Managers.md) / [IMTConManagerSink](../IMTConManagerSink.md) / OnManagerDelete

[Previous](OnManagerUpdate.md) | [Next](OnManagerSync.md)

# IMTConManagerSink::OnManagerDelete

A handler of the event of removing a manager configuration.

C++
    
    
    virtual void  IMTConManagerSink::OnManagerDelete(
       const IMTConManager*  config      // A pointer to the configuration object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConManagerSink.OnManagerDelete(
       CIMTConManager        config      // Configuration object
       )

### Parameters

**config**  
[in] A pointer to the object of the deleted manager configuration.

### Note

This method is called by the API to notify that a manager configuration has been deleted.
