[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Server Services](../Server-Services.md) / ServerRestart

[Previous](../Server-Services.md) | [Next](ServerRestartRemote.md)

# IMTServerAPI::ServerRestart

Restart the server on which the plugin is running.
    
    
    MTAPIRES  IMTServerAPI::ServerRestart()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred which corresponds to the response code.

### Note

When the main trade server is restarted from the API, other servers of the cluster are not restarted.
