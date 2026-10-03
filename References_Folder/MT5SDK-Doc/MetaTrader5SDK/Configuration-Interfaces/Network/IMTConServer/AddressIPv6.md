[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServer](../IMTConServer.md) / AddressIPv6

[Previous](AddressNext.md) | [Next](AddressIPv6Total.md)

# IMTConServer::Address

Get the IPv6 address of the server.

C++
    
    
    LPCWSTR  IMTConServer::Address()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConServer.Address()

Python (Manager API)
    
    
    MTConServer.AddressIPv6

### Return Value

If successful, it returns a pointer to the string with the server name. Otherwise, NULL is returned.

### Note

The address is specified in the format [address]:port.

# IMTConServer::Address

Set the IPv6 address of the server.

C++
    
    
    MTAPIRES  IMTConServer::Address(
       LPCWSTR  name      // Server address
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServer.Address(
       string   name      // Server address
       )

Python (Manager API)
    
    
    MTConServer.AddressIPv6

### Parameters

**name**  
[in] Server address.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The address is specified in the format [address]:port.
