[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServer](../IMTConServer.md) / Id

[Previous](AddressIPv6Next.md) | [Next](Password.md)

# IMTConServer::Id

Get the ID of the server.

C++
    
    
    UINT64  IMTConServer::Id()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConServer.Id()

Python (Manager API)
    
    
    MTConServer.Id

### Return Value

Server ID.

# IMTConServer::Id

Set the ID of the server.

C++
    
    
    MTAPIRES  IMTConServer::Id(
       UINT64  id      // Server ID
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServer.Id(
       ulong   id      // Server ID
       )

Python (Manager API)
    
    
    MTConServer.Id

### Parameters

**id**  
[in] Server ID.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
