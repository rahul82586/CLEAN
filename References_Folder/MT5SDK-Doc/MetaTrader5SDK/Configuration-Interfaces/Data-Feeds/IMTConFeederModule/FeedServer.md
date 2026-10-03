[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Data Feeds](../../Data-Feeds.md) / [IMTConFeederModule](../IMTConFeederModule.md) / FeedServer

[Previous](Module.md) | [Next](FeedLogin.md)

# IMTConFeederModule::FeedServer

Get the default address of the server to which the data feed module will connect.

C++
    
    
    LPCWSTR  IMTConFeederModule::FeedServer()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConFeederModule.FeedServer()

Python (Manager API)
    
    
    MTConFeederModule.FeedServer

### Return Value

If successful, it returns a pointer to a string with the default address of the server to which the data feed module will connect. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConModule](../IMTConFeederModule.md) object.
