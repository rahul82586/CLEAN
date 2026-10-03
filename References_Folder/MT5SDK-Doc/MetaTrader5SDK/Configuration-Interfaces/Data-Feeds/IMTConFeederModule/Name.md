[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Data Feeds](../../Data-Feeds.md) / [IMTConFeederModule](../IMTConFeederModule.md) / Name

[Previous](Clear.md) | [Next](Vendor.md)

# IMTConFeederModule::Name

Get the data feed name, which is inserted by default to a configuration when selecting this module.

C++
    
    
    LPCWSTR  IMTConFeederModule::Name()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConFeederModule.Name()

Python (Manager API)
    
    
    MTConFeederModule.Name

### Return Value

If successful, it returns a pointer to a string with the default name of the data feed. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConModule](../IMTConFeederModule.md) object.
