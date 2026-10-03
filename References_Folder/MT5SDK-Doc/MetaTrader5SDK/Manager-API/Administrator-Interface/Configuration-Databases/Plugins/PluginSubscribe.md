[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Plugins](../Plugins.md) / PluginSubscribe

[Previous](PluginParamCreate.md) | [Next](PluginUnsubscribe.md)

# IMTAdminAPI::PluginSubscribe

Subscribe to events associated with the configuration of plugins.

C++
    
    
    MTAPIRES  IMTAdminAPI::PluginSubscribe(
       IMTConPluginSink*  sink      // A pointer to the IMTConPluginSink object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.PluginSubscribe(
       CIMTConPluginSink  sink      // CIMTConPluginSink object
       )

Python
    
    
    AdminAPI.PluginSubscribe(
       sink      # IMTConPluginSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTConPluginSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Subscribing to events is thread safe. One and the same interface [IMTConPluginSink](../../../../Configuration-Interfaces/Plugins/IMTConPluginSink.md) cannot subscribe to an event twice - in this case the response code [MT_RET_ERR_DUPLICATE](../../../../Return-Codes/Common-errors.md) is returned.
