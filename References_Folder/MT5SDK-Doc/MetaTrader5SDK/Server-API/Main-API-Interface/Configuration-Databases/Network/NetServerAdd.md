[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Network](../Network.md) / NetServerAdd

[Previous](NetServerUnsubscribe.md) | [Next](NetServerDelete.md)

# IMTServerAPI::NetServerAdd

Add or update a server configuration.
    
    
    MTAPIRES  IMTServerAPI::NetServerAdd(
       IMTConServer*  config      // Server configuration object
       )

### Parameters

**config**  
[in] The server configuration object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

When calling the method, a check is made whether the entry already exists. If the entry already exists, it is updated, otherwise a new entry is added. A key field for comparison is the server ID [IMTConServer::Id()](../../../../Configuration-Interfaces/Network/IMTConServer/Id.md). When you try to add a completely identical record, no changes are made, and therefore the [IMTConServerSink::OnConServerUpdate](../../../../Configuration-Interfaces/Network/IMTConServerSink/OnConServerUpdate.md) notification method is not called.
