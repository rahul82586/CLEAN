[🏠 Document Start](../../README.md) / [Server API](../README.md) / [Plugin Interface](../Plugin-Interface.md) / Stop

[Previous](Start.md) | [Next](../Main-API-Interface.md)

# IMTServerPlugin::Stop

This method is called by the server before stopping and removing the plugin.
    
    
    MTAPIRES  IMTServerPlugin::Stop()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

By the time of call of the IMTServerPlugin::Stop method, the plugin automatically unsubscribes from all of the events to which it subscribed earlier. Thus you will get the [MT_RET_ERR_NOTFOUND](../../Return-Codes/Common-errors.md) error if you try to unsubscribe from an event within the implementation of the Stop method.
