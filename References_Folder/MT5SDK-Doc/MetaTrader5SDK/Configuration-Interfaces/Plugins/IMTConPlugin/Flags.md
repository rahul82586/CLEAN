[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Plugins](../../Plugins.md) / [IMTConPlugin](../IMTConPlugin.md) / Flags

[Previous](Mode.md) | [Next](ParameterAdd.md)

# IMTConPlugin::Flags

Get the plugin operation flags.

C++
    
    
    UINT  IMTConPlugin::Flags()  const

.NET (Gateway/Manager API)
    
    
    EnPluginFlags  CIMTConPlugin.Flags()

Python (Manager API)
    
    
    MTConPlugin.Flags

### Return Value

A value of the [IMTConPlugin::EnPluginFlags (#enpluginflags)](Enumerations.md#enpluginflags) enumeration.

# IMTConPlugin::Flags

Set the plugin operation flags.

C++
    
    
    MTAPIRES  IMTConPlugin::Flags(
       const UINT     flags    // Operation flags
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConPlugin.Flags(
       EnPluginFlags  flags    // Operation flags
       )

Python (Manager API)
    
    
    MTConPlugin.Flags

### Parameters

**mode**  
[in] TheIMTConPlugin::EnPluginFlagsenumeration is used to pass operation flags.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
