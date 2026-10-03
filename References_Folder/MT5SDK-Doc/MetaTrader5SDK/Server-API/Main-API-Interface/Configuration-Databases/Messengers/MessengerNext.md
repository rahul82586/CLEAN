[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Messengers](../Messengers.md) / MessengerNext

[Previous](MessengerTotal.md) | [Next](MessengerGet.md)

# IMTServerAPI::MessengerNext

Get a messenger configuration by index.
    
    
    MTAPIRES  IMTServerAPI::MessengerNext(
       const UINT        pos,       // Configuration position
       IMTConMessenger*  messenger  // Messenger configuration object
       )

### Parameters

**pos**  
[in] Position of the configuration, starting with 0.

**messenger**  
[out] Messenger configuration object. The 'messenger' object must be previously created using theIMTServerAPI::MessengerCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the configuration data of a messenger with a specified index to the 'messenger' object.
