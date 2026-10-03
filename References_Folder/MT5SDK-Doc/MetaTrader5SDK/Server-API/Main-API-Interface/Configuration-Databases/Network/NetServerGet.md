[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Network](../Network.md) / NetServerGet

[Previous](NetServerNext.md) | [Next](TLSCertificateUpdate.md)

# IMTServerAPI::NetServerGet

Get a server configuration by the ID.
    
    
    MTAPIRES  IMTServerAPI::NetServerGet(
       const UINT64   id,         // ID
       IMTConServer*  config      // Comment
       )

### Parameters

**id**  
[in] Server ID.

**config**  
[out] The server configuration object. The config object must first be created using theIMTServerAPI::NetServerCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The [IMTConServer::Id()](../../../../Configuration-Interfaces/Network/IMTConServer/Id.md) value is used as the ID.
