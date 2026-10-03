[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServer](../IMTConServer.md) / Name

[Previous](Type.md) | [Next](Address.md)

# IMTConServer::Name

Get the name of the server.

C++
    
    
    LPCWSTR  IMTConServer::Name()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConServer.Name()

Python (Manager API)
    
    
    MTConServer.Name

### Return Value

If successful, it returns a pointer to the string with the server name. Otherwise, it returns NULL.

### Note

The length of the server name is limited to 32 characters.

# IMTConServer::Name

Set the name of the server.

C++
    
    
    MTAPIRES  IMTConServer::Name(
       LPCWSTR  name      // Server name
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServer.Name(
       string   name      // Server name
       )

Python (Manager API)
    
    
    MTConServer.Name

### Parameters

**name**  
[in] Server name.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The length of the server name is limited to 32 characters.
