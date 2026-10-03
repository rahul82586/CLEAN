[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Plugins](../../Plugins.md) / [IMTConPluginModule](../IMTConPluginModule.md) / Name

[Previous](Clear.md) | [Next](Vendor.md)

# IMTConPluginModule::Name

Get the plugin name, which is inserted by default to a configuration when selecting this module.

C++
    
    
    LPCWSTR  IMTConPluginModule::Name()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConPluginModule.Name()

Python (Manager API)
    
    
    MTConPluginModule.Name()

### Return Value

If successful, it returns a pointer to a string with the default name of the plugin. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConPluginModule](../IMTConPluginModule.md) object.
