[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Plugins](../Plugins.md) / PluginGet

[Previous](PluginNext.md) | [Next](../Managers.md)

# IMTManagerAPI::PluginGet

Get the plugin configuration by the name.

C++
    
    
    MTAPIRES  IMTManagerAPI::PluginGet(
       LPCWSTR        name,          // Plugin configuration name
       IMTConPlugin*  plugin         // An object of a plugin configuration
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.PluginGet(
       string         name,          // Plugin configuration name
       CIMTConPlugin  plugin         // An object of a plugin configuration
       )

Python
    
    
    ManagerAPI.PluginGet(
       name           # Plugin configuration name
       )

### Parameters

**name**  
[in] Name of the plugin configuration. TheIMTConPlugin::Namevalue is used as the name.

**plugin**  
[out] An object of plugin configuration. The object must first be created using theIMTManagerAPI::PluginCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies parameters of the specified plugin configuration to the plugin object.
