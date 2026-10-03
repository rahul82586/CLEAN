[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Plugins](../../Plugins.md) / [IMTConPlugin](../IMTConPlugin.md) / ParameterAdd

[Previous](Flags.md) | [Next](ParameterUpdate.md)

# IMTConPlugin::ParameterAdd

Add a plugin parameter.

C++
    
    
    MTAPIRES  IMTConPlugin::ParameterAdd(
       IMTConParam*  param      // An object of the plugin parameter
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConPlugin.ParameterAdd(
       CIMTConParam  param      // An object of the plugin parameter
       )

Python (Manager API)
    
    
    MTConPlugin.ParameterAdd(
       param         # An object of the plugin parameter
       )

### Parameters

**param**  
[in] An object of a plugin parameterIMTConParam.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, a corresponding error code will be returned.

### Note

You can add a maximum of 128 parameters for a plugin.
