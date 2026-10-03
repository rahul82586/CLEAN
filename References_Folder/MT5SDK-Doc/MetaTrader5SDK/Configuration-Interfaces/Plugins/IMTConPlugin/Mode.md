[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Plugins](../../Plugins.md) / [IMTConPlugin](../IMTConPlugin.md) / Mode

[Previous](Module.md) | [Next](Flags.md)

# IMTConPlugin::Mode

Get the plugin operation mode.

C++
    
    
    UINT  IMTConPlugin::Mode()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConPlugin.Mode()

Python (Manager API)
    
    
    MTConPlugin.Mode

### Return Value

A value of the [IMTConPlugin::EnPluginMode (#enpluginmode)](Enumerations.md#enpluginmode) enumeration.

# IMTConPlugin::Mode

Get the plugin operation mode.

C++
    
    
    MTAPIRES  IMTConPlugin::Mode(
       const UINT  mode      // Operation mode
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConPlugin.Mode(
       uint        mode      // Operation mode
       )

Python (Manager API)
    
    
    MTConPlugin.Mode

### Parameters

**mode**  
[in] TheIMTConPlugin::EnPluginModeenumeration is used to pass the operation mode.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
