[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Network](../Network.md) / NetServerRestart

[Previous](NetServerUnsubscribe.md) | [Next](NetServerUpdate.md)

# IMTAdminAPI::NetServerRestart

Restart a server by an ID.

C++
    
    
    MTAPIRES  IMTAdminAPI::NetServerRestart(
       const UINT64  id      // Server ID
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.NetServerRestart(
       ulong         id      // Server ID
       )

Python
    
    
    AdminAPI.NetServerRestart(
       id            # Server ID
       )

### Parameters

**id**  
[in] The identifier of the server that should be restarted. TheIMTConServer::Idvalue is used as the identifier.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Restart servers only on weekends and holidays or at night when the trading activity is minimal. Restarting the server may take several seconds (up to a minute), during this time connection to the server is impossible.
