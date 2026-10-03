[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServer](../IMTConServer.md) / AdaptersNext

[Previous](AdaptersTotal.md) | [Next](Version.md)

# IMTConServer::AdaptersNext

Get the network controller by the index.

C++
    
    
    LPCWSTR  IMTConServer::AdaptersNext(
       const UINT  pos      // Position of the network controller
       )  const

.NET (Gateway/Manager API)
    
    
    string  IMTConServer::AdaptersNext(
       uint        pos      // Position of the network controller
       )

Python (Manager API)
    
    
    MTConServer.AdaptersNext(
       pos         # Position of the network controller
       )

### Parameters

**pos**  
[in] Position of a network controller in the list, starting with 0.

### Return Value

If successful, it returns a pointer to a string with the name of the network controller. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConServer](../IMTConServer.md) object.

To use the string after the object removal (call of the [IMTConServer::Release](Release.md) method of this object), a copy of it should be created.

The length of the controller name is limited to 128 characters (including the end-of-line character).
