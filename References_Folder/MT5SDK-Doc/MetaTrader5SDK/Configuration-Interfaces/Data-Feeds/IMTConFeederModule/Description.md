[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Data Feeds](../../Data-Feeds.md) / [IMTConFeederModule](../IMTConFeederModule.md) / Description

[Previous](Vendor.md) | [Next](Module.md)

# IMTConFeederModule::Description

Get the description of the data feed module.

C++
    
    
    LPCWSTR  IMTConFeederModule::Description()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConFeederModule.Description()

Python (Manager API)
    
    
    MTConFeederModule.Description

### Return Value

If successful, it returns a pointer to a string with the description of the data feed module. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConModule](../IMTConFeederModule.md) object.

To use the string after the object removal (call of the [IMTConFeederModule::Release](Release.md) method of this object), a copy of it should be created.

The description length is limited to 512 characters (including the end-of-line character).
