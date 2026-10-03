[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServer](../IMTConServer.md) / BuildDate

[Previous](Build.md) | [Next](LastBootTime.md)

# IMTConServer::BuildDate

Get the date of the server build.

C++
    
    
    LPCWSTR  IMTConServer::BuildDate()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConServer.BuildDate()

Python (Manager API)
    
    
    MTConServer.BuildDate

### Return Value

If successful, it returns a pointer to the string with the server build date. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConServer](../IMTConServer.md) object.
