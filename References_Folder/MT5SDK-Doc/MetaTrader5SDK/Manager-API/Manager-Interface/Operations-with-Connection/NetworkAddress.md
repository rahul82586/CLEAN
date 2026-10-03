[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Operations with Connection](../Operations-with-Connection.md) / NetworkAddress

[Previous](NetworkServer.md) | [Next](../Configuration-Databases.md)

# IMTManagerAPI::NetworkAddress

Receive IP address of the server Manager API is currently connected to.

C++
    
    
    MTAPIRES  IMTManagerAPI::NetworkAddress(
       MTAPISTR&   address      // Server address
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.NetworkAddress(
       out string  address      // Server address
       )

Python
    
    
    ManagerAPI.NetworkAddress()

### Parameters

**address**  
[out] A reference to the IP address of the server Manager API is connected to.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### 
