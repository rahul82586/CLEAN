[🏠 Document Start](../../README.md) / [Server API](../README.md) / [Entry Points](../Entry-Points.md) / MTServerCreate

[Previous](MTServerAbout.md) | [Next](../Plugin-Interface.md)

# MTServerCreate

The MTServerCreate Entry Point. This method is called by the server to create an instance of an object of the server plugin that implements the [IMTServerPlugin](../Plugin-Interface.md) interface.
    
    
    MTAPIENTRY MTAPIRES  MTServerCreate(
       UINT               apiversion,     // API Version
       IMTServerPlugin**  plugin          // Pointer to a pointer to the plugin
       )

### Parameters

**apiversion**  
[in] The current version of the Server API supported by the server is passed in this parameter.

**plugin**  
[out] A pointer to a pointer to the plugin. The created instance of the server plugin should be placed in this parameter.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, corresponding to the response code.
