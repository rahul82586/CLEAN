[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Plugins](../../Plugins.md) / [IMTConPlugin](../IMTConPlugin.md) / Name

[Previous](Clear.md) | [Next](Server.md)

# IMTConPlugin::Name

Get the name of a plugin.

C++
    
    
    LPCWSTR  IMTConPlugin::Name()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConPlugin.Name()

Python (Manager API)
    
    
    MTConPlugin.Name

### Return Value

If successful, it returns a pointer to a string with the name of a plugin. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConPlugin](../IMTConPlugin.md) object.

# IMTConPlugin::Name

Set the name of a plugin.

C++
    
    
    MTAPIRES  IMTConPlugin::Name(
       LPCWSTR  name      // Plugin name
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConPlugin.Name(
       string   name      // Plugin name
       )

Python (Manager API)
    
    
    MTConPlugin.Name

### Parameters

**name**  
[in] The name of a plugin.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The maximum name length is 16 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
