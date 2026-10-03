[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Plugins](../Plugins.md) / PluginShift

[Previous](PluginDeleteBatch.md) | [Next](PluginTotal.md)

# IMTAdminAPI::PluginShift

Changes the position of a plugin configuration in the list.

C++
    
    
    MTAPIRES  IMTAdminAPI::PluginShift(
       const UINT  pos,       // Position of the configuration
       const int   shift      // Shift
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.PluginShift(
       uint        pos,       // Position of the configuration
       int         shift      // Shift
       )

Python
    
    
    AdminAPI.PluginShift(
       pos,        # Position of the configuration
       shift       # Shift
       )

### Parameters

**pos**  
[in] Position of the configuration, starting with 0.

**shift**  
[in] Shift of the configuration relative to its current position. A negative value means the shift to the top of the list, a positive value - to its end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The position of a configuration can be changed only from the applications that run on the main server. For all other applications the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) will be returned.
