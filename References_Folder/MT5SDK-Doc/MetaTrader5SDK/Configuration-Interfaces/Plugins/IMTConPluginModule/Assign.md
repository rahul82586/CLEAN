[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Plugins](../../Plugins.md) / [IMTConPluginModule](../IMTConPluginModule.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTConPluginModule::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTConPluginModule::Assign(
       const IMTConPluginModule*  param      // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConPluginModule.Assign(
       CIMTConPluginModule        param      // Source object
       )

### Parameters

**param**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
