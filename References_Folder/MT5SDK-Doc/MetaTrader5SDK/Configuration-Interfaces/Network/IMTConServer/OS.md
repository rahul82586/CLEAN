[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServer](../IMTConServer.md) / OS

[Previous](Connected.md) | [Next](CPU.md)

# IMTConServer::OS

Get the operating system of the computer running the server.

C++
    
    
    LPCWSTR  IMTConServer::OS()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConServer.OS()

Python (Manager API)
    
    
    MTConServer.OS

### Return Value

If successful, it returns a pointer to the string with the operating system. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConServer](../IMTConServer.md) object.
