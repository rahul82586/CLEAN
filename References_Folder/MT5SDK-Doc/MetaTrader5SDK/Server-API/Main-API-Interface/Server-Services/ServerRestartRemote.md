[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Server Services](../Server-Services.md) / ServerRestartRemote

[Previous](ServerRestart.md) | [Next](ServerSubscribe.md)

# IMTServerAPI::ServerRestartRemote

Restart the server with the specified identifier.
    
    
    MTAPIRES  IMTServerAPI::ServerRestartRemote(
       const UINT64  id,            // Server ID
       reason        reason         // Reason for restart
       )

### Parameters

**id**  
[in] The identifier of the server to be restarted (IMTConServer::Id)

**reason**  
[in] Description of the reason for restarting the server. This reason will be printed to the server log.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

When the main trade server is restarted from the API, other servers of the cluster are not restarted.
