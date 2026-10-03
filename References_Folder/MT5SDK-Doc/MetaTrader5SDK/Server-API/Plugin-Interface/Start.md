[🏠 Document Start](../../README.md) / [Server API](../README.md) / [Plugin Interface](../Plugin-Interface.md) / Start

[Previous](Release.md) | [Next](Stop.md)

# IMTServerPlugin::Start

This method is called by the server during the plugin start.
    
    
    MTAPIRES  IMTServerPlugin::Start(
       IMTServerAPI*  server      // Pointer to the API interface
       )

### Parameters

**server**  
[in] Pointer to the interface of the Server API.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../Return-Codes/Successful-completion.md) response code. If the return code is different from MT_RET_OK, the plugin will not be loaded, and its object will be destroyed.

### Note

A plugin starts processing of [events (#events)](../Creating-a-Simple-Plugin.md#events) only after the Start method is executed.
