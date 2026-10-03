[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServer](../IMTConServer.md) / Address

[Previous](Name.md) | [Next](AddressTotal.md)

# IMTConServer::Address

Get the IPv4 address of the server.

C++
    
    
    LPCWSTR  IMTConServer::Address()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConServer.Address()

Python (Manager API)
    
    
    MTConServer.Address

### Return Value

If successful, it returns a pointer to the string with the server name. Otherwise, it returns NULL.

### Note

The address is specified in the format address:port.

# IMTConServer::Address

Set the IPv4 address of the server.

C++
    
    
    MTAPIRES  IMTConServer::Address(
       LPCWSTR  name      // Server address
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServer.Address(
       string   name      // Server address
       )

Python (Manager API)
    
    
    MTConServer.Address

### Parameters

**name**  
[in] Server address.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The address is specified in the format address:port.
