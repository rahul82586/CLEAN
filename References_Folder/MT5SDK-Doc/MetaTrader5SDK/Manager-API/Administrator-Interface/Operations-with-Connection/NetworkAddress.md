[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Operations with Connection](../Operations-with-Connection.md) / NetworkAddress

[Previous](NetworkServer.md) | [Next](../Server-Management.md)

# IMTAdminAPI::NetworkAddress

Receive IP address of the server Manager API is currently connected to.

C++
    
    
    MTAPIRES  IMTAdminAPI::NetworkAddress(
       MTAPISTR&  address      // Server address
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.NetworkAddress(
       out sting  address      // Server address
       )

Python
    
    
    AdminAPI.NetworkAddress()

### Parameters

**address**  
[out] A reference to the IP address of the server Manager API is connected to.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### 
