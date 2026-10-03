[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Data Feeds](../../Data-Feeds.md) / [IMTConFeederModule](../IMTConFeederModule.md) / FeedLogin

[Previous](FeedServer.md) | [Next](FeedPassword.md)

# IMTConFeederModule::FeedLogin

Get a default login that will be used by a data feed to connect to the server.

C++
    
    
    LPCWSTR  IMTConFeederModule::FeedLogin()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConFeederModule.FeedLogin()

Python (Manager API)
    
    
    MTConFeederModule.FeedLogin

### Return Value

If successful, it returns a pointer to a string with the default login, which will be used by the data feed to connect to the server. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConModule](../IMTConFeederModule.md) object.
