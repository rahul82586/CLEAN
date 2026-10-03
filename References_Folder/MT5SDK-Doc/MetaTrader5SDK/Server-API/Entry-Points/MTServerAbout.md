[🏠 Document Start](../../README.md) / [Server API](../README.md) / [Entry Points](../Entry-Points.md) / MTServerAbout

[Previous](../Entry-Points.md) | [Next](MTServerCreate.md)

# MTServerAbout

The MTServerCreateAbout entry point provides the server with the initial information about the plugin.
    
    
    MTAPIENTRY MTAPIRES  MTServerAbout(
       MTPluginInfo&  info      // Reference to MTPluginInfo
       )

### Parameters

**info**  
[out] A reference to theMTPluginInfostructure.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../Return-Codes/Successful-completion.md) response code. If the return code is different from MT_RET_OK, the plug will not appear in the list of modules.

### Note

The plugin must correctly fill in the [MTPluginInfo](../../Structures/MTPluginInfo.md) structure.
