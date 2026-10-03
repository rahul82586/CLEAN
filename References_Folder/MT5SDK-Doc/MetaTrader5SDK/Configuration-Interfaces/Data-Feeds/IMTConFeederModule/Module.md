[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Data Feeds](../../Data-Feeds.md) / [IMTConFeederModule](../IMTConFeederModule.md) / Module

[Previous](Description.md) | [Next](FeedServer.md)

# IMTConFeederModule::Module

Get the name of the file of the data feed module.

C++
    
    
    LPCWSTR  IMTConFeederModule::Module()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConFeederModule.Module()

Python (Manager API)
    
    
    MTConFeederModule.Module

### Return Value

If successful, it returns a pointer to a string with the file name of the data feed module. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConModule](../IMTConFeederModule.md) object.
