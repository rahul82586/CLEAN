[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Data Feeds](../../Data-Feeds.md) / [IMTConFeederModule](../IMTConFeederModule.md) / FeedPassword

[Previous](FeedLogin.md) | [Next](Version.md)

# IMTConFeederModule::FeedPassword

Get a default password that will be used by a data feed to connect to the server.

C++
    
    
    LPCWSTR  IMTConFeederModule::FeedPassword()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConFeederModule.FeedPassword()

Python (Manager API)
    
    
    MTConFeederModule.FeedPassword

### Return Value

If successful, it returns a pointer to a string with the default password, which will be used by the data feed to connect to the server. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConModule](../IMTConFeederModule.md) object.
