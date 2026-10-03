[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Plugins](../Plugins.md) / PluginUpdate

[Previous](PluginParamCreate.md) | [Next](PluginTotal.md)

# IMTManagerAPI::PluginUpdate

Update a plugin configuration.

C++
    
    
    MTAPIRES  IMTManagerAPI::PluginUpdate(
       IMTConPlugin*  plugin      // An object of a plugin configuration
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.PluginUpdate(
       CIMTConPlugin  plugin      // An object of a plugin configuration
       )

Python
    
    
    ManagerAPI.PluginUpdate(
       plugin         # An object of a plugin configuration
       )

### Parameters

**plugin**  
[in] An object of plugin configuration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Before adding, the correctness of the record is checked. If the record is incorrect, the error code [MT_RET_ERR_PARAMS](../../../../Return-Codes/Common-errors.md) is returned.
