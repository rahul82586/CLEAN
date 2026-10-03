[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Managers](../../Managers.md) / [IMTConManagerSink](../IMTConManagerSink.md) / OnManagerAdd

[Previous](../IMTConManagerSink.md) | [Next](OnManagerUpdate.md)

# IMTConManagerSink::OnManagerAdd

A handler of the event of adding a new manager configuration.

C++
    
    
    virtual void  IMTConManagerSink::OnManagerAdd(
       const IMTConManager*  config      // A pointer to the configuration object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConManagerSink.OnManagerAdd(
       CIMTConManager        config      // Configuration object
       )

### Parameters

**config**  
[in] A pointer to the object of the added manager configuration.

### Note

This method is called by the API to notify that a new manager configuration has been added.
