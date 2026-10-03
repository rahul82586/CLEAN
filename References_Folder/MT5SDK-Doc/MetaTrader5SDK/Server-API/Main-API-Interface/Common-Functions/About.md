[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Common Functions](../Common-Functions.md) / About

[Previous](LoggerFlush.md) | [Next](LicenseCheck.md)

# IMTServerAPI::About

Quickly receive the description of the server on which the plugin is running.
    
    
    MTAPIRES  IMTServerAPI::About(
       MTServerInfo&  info      // Pointer to MTServerInfo
       )

### Parameters

**info**  
[in] A pointer to theMTServerInfostructure.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This function copies the [MTServerInfo](../../../Structures/MTServerInfo.md) structure to the info parameter.
