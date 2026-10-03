[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Plugins](../../Plugins.md) / [IMTConPluginModule](../IMTConPluginModule.md) / Module

[Previous](Description.md) | [Next](Server.md)

# IMTConPluginModule::Module

Get the name of the plugin module file.

C++
    
    
    LPCWSTR  IMTConPluginModule::Module()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConPluginModule.Module()

Python (Manager API)
    
    
    MTConPluginModule.Module()

### Return Value

If successful, it returns a pointer to a string with the file name of the plugin module. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConPluginModule](../IMTConPluginModule.md) object.
