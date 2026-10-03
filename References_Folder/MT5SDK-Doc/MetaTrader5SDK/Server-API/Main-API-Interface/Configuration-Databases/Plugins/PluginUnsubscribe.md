[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Plugins](../Plugins.md) / PluginUnsubscribe

[Previous](PluginSubscribe.md) | [Next](PluginCurrent.md)

# IMTServerAPI::PluginUnsubscribe

Unsubscribe from events and hooks associated with the configuration of plugins.
    
    
    MTAPIRES  IMTServerAPI::PluginUnsubscribe(
       IMTConPluginSink*  sink      // A pointer to the IMTConPluginSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTConPluginSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This is a pair method to [IMTServerAPI::PluginSubscribe](PluginSubscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) error is returned.
