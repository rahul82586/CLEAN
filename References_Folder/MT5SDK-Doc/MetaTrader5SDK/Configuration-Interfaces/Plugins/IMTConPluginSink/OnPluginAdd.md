[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Plugins](../../Plugins.md) / [IMTConPluginSink](../IMTConPluginSink.md) / OnPluginAdd

[Previous](../IMTConPluginSink.md) | [Next](OnPluginUpdate.md)

# IMTConPluginSink::OnPluginAdd

A handler of the event of adding a new plugin configuration.

C++
    
    
    virtual void  IMTConPluginSink::OnPluginAdd(
       const IMTConPlugin*  plugin      // A pointer to the configuration module
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConPluginSink.OnPluginAdd(
       CIMTConPlugin        plugin      // Configuration object
       )

### Parameters

**plugin**  
[in] A pointer to the object of the added configuration.

### Note

This method is called by the API to notify of adding of a new plugin configuration.
