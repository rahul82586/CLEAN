[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Operations with Connection](../Operations-with-Connection.md) / NetworkServer

[Previous](NetworkBytesRead.md) | [Next](NetworkAddress.md)

# IMTManagerAPI::NetworkServer

Receive the name of the server Manager API is currently connected to.

C++
    
    
    MTAPIRES  IMTManagerAPI::NetworkServer(
       MTAPISTR&   server      // Server name
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.NetworkServer(
       out string  server      // Server name
       )

Python
    
    
    ManagerAPI.NetworkServer()

### Parameters

**server**  
[out] A reference to the name of the server Manager API is connected to.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### 
