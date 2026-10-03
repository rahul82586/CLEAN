[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Plugins](../../Plugins.md) / [IMTConPlugin](../IMTConPlugin.md) / ParameterClear

[Previous](ParameterDelete.md) | [Next](ParameterShift.md)

# IMTConPlugin::ParameterClear

Clear the list of plugin parameters.

C++
    
    
    MTAPIRES  IMTConPlugin::ParameterClear()  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConPlugin.ParameterClear()

Python (Manager API)
    
    
    MTConPlugin.ParameterClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method clears the entire list of plugin parameters.
