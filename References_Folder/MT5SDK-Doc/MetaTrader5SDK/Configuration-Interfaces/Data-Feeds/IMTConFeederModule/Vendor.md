[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Data Feeds](../../Data-Feeds.md) / [IMTConFeederModule](../IMTConFeederModule.md) / Vendor

[Previous](Name.md) | [Next](Description.md)

# IMTConFeederModule::Vendor

Get the name of the provider of the data feed module.

C++
    
    
    LPCWSTR  IMTConFeederModule::Vendor()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConFeederModule.Vendor()

Python (Manager API)
    
    
    MTConFeederModule.Vendor

### Return Value

If successful, it returns a pointer to a string with the name of the provider of the data feed module. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConModule](../IMTConFeederModule.md) object.
