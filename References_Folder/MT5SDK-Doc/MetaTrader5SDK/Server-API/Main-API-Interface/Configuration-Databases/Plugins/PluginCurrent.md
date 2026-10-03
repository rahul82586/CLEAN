[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Plugins](../Plugins.md) / PluginCurrent

[Previous](PluginUnsubscribe.md) | [Next](PluginAdd.md)

# IMTServerAPI::PluginCurrent

Get the configuration of the current plugin.
    
    
    MTAPIRES  IMTServerAPI::PluginCurrent(
       IMTConPlugin*  plugin      // An object of a plugin configuration
       )

### Parameters

**plugin**  
[out] An object of plugin configuration. The plugin object must be first created using theIMTServerAPI::PluginCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the configuration data of the current plugin to the plugin object.
