[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Operations with Connection](../Operations-with-Connection.md) / NetworkServer

[Previous](NetworkBytesRead.md) | [Next](NetworkAddress.md)

# IMTAdminAPI::NetworkServer

Receive the name of the server Manager API is currently connected to.
    
    
    MTAPIRES  IMTAdminAPI::NetworkServer(
       MTAPISTR&  server      // server name
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.NetworkServer(
       out string  server     // server name
       )

Python
    
    
    AdminAPI.NetworkServer()

### Parameters

**server**  
[out] A reference to the name of the server Manager API is connected to.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### 
