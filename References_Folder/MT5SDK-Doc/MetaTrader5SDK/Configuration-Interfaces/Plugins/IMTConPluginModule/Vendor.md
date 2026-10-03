[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Plugins](../../Plugins.md) / [IMTConPluginModule](../IMTConPluginModule.md) / Vendor

[Previous](Name.md) | [Next](Description.md)

# IMTConPluginModule::Vendor

Get the name of the plugin module provider.

C++
    
    
    LPCWSTR  IMTConPluginModule::Vendor()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConPluginModule.Vendor()

Python (Manager API)
    
    
    MTConPluginModule.Vendor()

### Return Value

If successful, it returns a pointer to a string with the file name of the plugin module provider. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConPluginModule](../IMTConPluginModule.md) object.
