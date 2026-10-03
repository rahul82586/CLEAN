[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Plugins](../../Plugins.md) / [IMTConPlugin](../IMTConPlugin.md) / Module

[Previous](Server.md) | [Next](Mode.md)

# IMTConPlugin::Module

Get the name of a plugin module.

C++
    
    
    LPCWSTR  IMTConPlugin::Module()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConPlugin.Module()

Python (Manager API)
    
    
    MTConPlugin.Module

### Return Value

If successful, it returns a pointer to a string with the name of a plugin module. Otherwise, it returns NULL.

### Note

It returns the name of the module (DLL) that corresponds to the plugin.

The pointer to the resulting string is valid for the lifetime of the [IMTConPlugin](../IMTConPlugin.md) object.

To use the line after the object removal (call of the [IMTConPlugin::Release](Release.md) method of this object), a copy of it should be created.

# IMTConPlugin::Module

Set the name of a plugin module.

C++
    
    
    MTAPIRES  IMTConPlugin::Module(
       LPCWSTR  name      // The name of the plugin module
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConPlugin.Module(
       string   name      // The name of the plugin module
       )

Python (Manager API)
    
    
    MTConPlugin.Module

### Parameters

**name**  
[in] The name of a plugin module.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The maximum name length is 64 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
