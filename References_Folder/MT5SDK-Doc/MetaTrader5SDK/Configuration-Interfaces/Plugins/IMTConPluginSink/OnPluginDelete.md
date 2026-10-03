[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Plugins](../../Plugins.md) / [IMTConPluginSink](../IMTConPluginSink.md) / OnPluginDelete

[Previous](OnPluginUpdate.md) | [Next](OnPluginSync.md)

# IMTConPluginSink::OnPluginDelete

A handler of the event of removing a plugin configuration.

C++
    
    
    virtual void  IMTConPluginSink::OnPluginDelete(
       const IMTConPlugin*  plugin      // A pointer to the configuration module
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConPluginSink.OnPluginDelete(
       CIMTConPlugin        plugin      // Configuration object
       )

### Parameters

**plugin**  
[in] A pointer to the object of the deleted configuration.

### Note

This method is called by the API to notify of the fact that a plugin configuration has been deleted.
