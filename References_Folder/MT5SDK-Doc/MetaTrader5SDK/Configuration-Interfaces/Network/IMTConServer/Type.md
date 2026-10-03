[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServer](../IMTConServer.md) / Type

[Previous](Clear.md) | [Next](Name.md)

# IMTConServer::Type

Get the address of the server.

C++
    
    
    UINT  IMTConServer::Type()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConServer.Type()

Python (Manager API)
    
    
    MTConServer.Type

### Return Value

One of the values of the [IMTConServer::EnServerTypes (#enservertypes)](Enumerations.md#enservertypes) enumeration.

# IMTConServer::Type

Set the server type.

C++
    
    
    MTAPIRES  IMTConServer::Type(
       const UINT  type      // Server type
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServer.Type(
       uint        type      // Server type
       )

Python (Manager API)
    
    
    MTConServer.Type

### Parameters

**type**  
[in] The server type is passed using theIMTConServer::EnServerTypesenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
