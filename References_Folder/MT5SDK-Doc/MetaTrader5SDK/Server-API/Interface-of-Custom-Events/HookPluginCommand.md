[🏠 Document Start](../../README.md) / [Server API](../README.md) / [Interface of Custom Events](../Interface-of-Custom-Events.md) / HookPluginCommand

[Previous](HookWebAPICommand.md) | [Next](../Interface-of-Trade-Events.md)

# IMTCustomSink::HookPluginCommand

Hook for the execution of a [custom command](../Main-API-Interface/Custom-Functions/CustomCommand.md) transmitted by the plugin from another server within the cluster.
    
    
    MTAPIRES  IMTCustomSink::HookPluginCommand(
       const IMTConPlugin*   manager,         // plugin configuration object
       IMTByteStream*        indata,          // input data
       IMTByteStream*        outdata,         // output data
       )

### Parameters

**manager**  
[in] TheIMTConPluginobject describing the configuration the plugin that sent the custom command.

**indata**  
[in]Object of the data streamtransmitted to the server.

**outdata**  
[out] A pointer to theobject of the data streamreturned in response to the command.

### Return Value

If the hook does not handle the event, it returns [MT_RET_OK_NONE](../../Return-Codes/Successful-completion.md). If the event is processed, the returned response code is sent along with the 'outdata' buffer to the plugin that called the custom command.

### Note

The hook is called sequentially, following the order of the plugins in the list, until it reaches the plugin that returns a response code other than [MT_RET_OK_NONE](../../Return-Codes/Successful-completion.md).
