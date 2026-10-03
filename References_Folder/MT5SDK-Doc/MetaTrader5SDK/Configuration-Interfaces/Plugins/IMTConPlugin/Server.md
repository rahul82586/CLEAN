[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Plugins](../../Plugins.md) / [IMTConPlugin](../IMTConPlugin.md) / Server

[Previous](Name.md) | [Next](Module.md)

# IMTConPlugin::Server

Get the ID of the server on which the plugin is installed.

C++
    
    
    UINT64  IMTConPlugin::Server()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConPlugin.Server()

Python (Manager API)
    
    
    MTConPlugin.Server

### Return Value

The ID of the server on which the plugin module is installed.

# IMTConPlugin::Server

Set the ID of the server.

C++
    
    
    MTAPIRES  IMTConPlugin::Server(
       const UINT64  server      // Server ID
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConPlugin.Server(
       ulong         server      // Server ID
       )

Python (Manager API)
    
    
    MTConPlugin.Server

### Parameters

**server**  
[in] Server ID.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
