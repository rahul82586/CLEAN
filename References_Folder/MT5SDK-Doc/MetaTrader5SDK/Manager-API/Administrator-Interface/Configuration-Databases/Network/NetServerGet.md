[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Network](../Network.md) / NetServerGet

[Previous](NetServerNext.md) | [Next](TLSCertificateUpdate.md)

# IMTAdminAPI::NetServerGet

Get a server configuration by the ID.

C++
    
    
    MTAPIRES  IMTAdminAPI::NetServerGet(
       const UINT64   id,         // ID
       IMTConServer*  config      // Comment
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.NetServerGet(
       ulong          id,         // ID
       CIMTConServer  config      // Comment
       )

Python
    
    
    AdminAPI.NetServerGet(
       id             # ID
       )

### Parameters

**id**  
[in] Server ID.

**config**  
[out] The server configuration object. The config object must first be created using theIMTAdminAPI::NetServerCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The [IMTConServer::Id()](../../../../Configuration-Interfaces/Network/IMTConServer/Id.md) value is used as the ID.
