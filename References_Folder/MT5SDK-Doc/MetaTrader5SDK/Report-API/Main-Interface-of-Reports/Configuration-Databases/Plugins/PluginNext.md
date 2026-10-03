[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Configuration Databases](../../Configuration-Databases.md) / [Plugins](../Plugins.md) / PluginNext

[Previous](PluginTotal.md) | [Next](PluginGet.md)

# IMTReportAPI::PluginNext

Get the plugin configuration by the index.
    
    
    MTAPIRES  IMTReportAPI::PluginNext(
       const UINT     pos,        // Position of the configuration
       IMTConPlugin*  plugin      // An object of a plugin configuration
       )

### Parameters

**pos**  
[in] Position of the configuration, starting with 0.

**plugin**  
[out] An object of plugin configuration. The plugin object must be first created using theIMTReportAPI::PluginCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the configuration data of a plugin with a specified index to the plugin object.
