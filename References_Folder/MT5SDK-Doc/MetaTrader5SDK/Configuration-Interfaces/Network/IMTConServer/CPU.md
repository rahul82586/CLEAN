[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServer](../IMTConServer.md) / CPU

[Previous](OS.md) | [Next](CPUTotal.md)

# IMTConServer::CPU

Get the processor type of the computer that is running the server.

C++
    
    
    LPCWSTR  IMTConServer::CPU()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConServer.CPU()

Python (Manager API)
    
    
    MTConServer.CPU

### Return Value

If successful, it returns a pointer to the string with the processor. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConServer](../IMTConServer.md) object.

To use the string after the object removal (call of the [IMTConServer::Release](Release.md) method of this object), a copy of it should be created.

The length of the processor type is limited to 64 characters (including the end-of-line character).
