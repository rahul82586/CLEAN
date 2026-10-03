[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Plugins](../../Plugins.md) / [IMTConPlugin](../IMTConPlugin.md) / ParameterUpdate

[Previous](ParameterAdd.md) | [Next](ParameterDelete.md)

# IMTConPlugin::ParameterUpdate

Update the parameter of a plugin in the list.

C++
    
    
    MTAPIRES  IMTConPlugin::ParameterUpdate(
       const UINT          pos,       // Position of the parameter
       const IMTConParam*  param      // An object of the plugin parameter
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConPlugin.ParameterUpdate(
       uint                pos,       // Position of the parameter
       CIMTConParam        param      // An object of the plugin parameter
       )

Python (Manager API)
    
    
    MTConPlugin.ParameterUpdate(
       pos,                # Position of the parameter
       param               # An object of the plugin parameter
       )

### Parameters

**pos**  
[in] Position of the parameter, starting with 0.

**param**  
[in] An object of a plugin parameter.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
