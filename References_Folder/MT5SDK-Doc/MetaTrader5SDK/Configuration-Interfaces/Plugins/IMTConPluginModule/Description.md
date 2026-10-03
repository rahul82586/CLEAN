[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Plugins](../../Plugins.md) / [IMTConPluginModule](../IMTConPluginModule.md) / Description

[Previous](Vendor.md) | [Next](Module.md)

# IMTConPluginModule::Description

Get the description of a plugin module.

C++
    
    
    LPCWSTR  IMTConPluginModule::Description()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConPluginModule.Description()

Python (Manager API)
    
    
    MTConPluginModule.Description()

### Return Value

If successful, it returns a pointer to a string with the description of the plugin module. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConPluginModule](../IMTConPluginModule.md) object.
