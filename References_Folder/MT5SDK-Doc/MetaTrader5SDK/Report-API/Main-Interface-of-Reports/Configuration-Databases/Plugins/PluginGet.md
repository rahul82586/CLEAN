[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Configuration Databases](../../Configuration-Databases.md) / [Plugins](../Plugins.md) / PluginGet

[Previous](PluginNext.md) | [Next](PluginModuleTotal.md)

# IMTReportAPI::PluginGet

Get the plugin configuration by the name.
    
    
    virtual MTAPIRES  IMTReportAPI::PluginGet(
       const UINT64   server_id,     // Server ID
       LPCWSTR        name,          // Plugin configuration name
       IMTConPlugin*  plugin         // An object of a plugin configuration
       )

### Parameters

**server_id**  
[in] The identifier of the server for which we get the plugin configuration. TheIMTConServer::Idvalue is used as the identifier.

**name**  
[in] Name of the plugin configuration. TheIMTConPlugin::Namevalue is used as the name.

**plugin**  
[out] An object of plugin configuration. The object must first be created using theIMTReportAPI::PluginCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies parameters of the specified plugin configuration to the plugin object.
