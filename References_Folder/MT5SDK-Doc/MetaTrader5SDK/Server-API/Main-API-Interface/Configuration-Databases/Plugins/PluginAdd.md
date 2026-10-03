[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Plugins](../Plugins.md) / PluginAdd

[Previous](PluginCurrent.md) | [Next](PluginDelete.md)

# IMTServerAPI::PluginAdd

Add or update a plugin configuration.
    
    
    MTAPIRES  IMTServerAPI::PluginAdd(
       IMTConPlugin*  plugin      // An object of a plugin configuration
       )

### Parameters

**plugin**  
[in] An object of plugin configuration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

When calling the method, a check is made whether the entry already exists. If the entry already exists, it is updated, otherwise a new entry is added. A key field for comparison is the name of the configuration [IMTConPlugin::Name()](../../../../Configuration-Interfaces/Plugins/IMTConPlugin/Name.md). When you try to add a completely identical record, no changes are made, and therefore the [IMTConPluginSink::OnPluginUpdate](../../../../Configuration-Interfaces/Plugins/IMTConPluginSink/OnPluginUpdate.md) notification method is not called.
