[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Messengers](../Messengers.md) / MessengerGet

[Previous](MessengerNext.md) | [Next](MessengerVerifyPhone.md)

# IMTServerAPI::MessengerGet

Get a messenger configuration by name.
    
    
    MTAPIRES  IMTServerAPI::MessengerGet(
       LPCWSTR           name,      // Configuration name
       IMTConMessenger*  messenger  // Messenger configuration object
       )

### Parameters

**name**  
[in] The name of the configuration.

**messenger**  
[out] Messenger configuration object. The 'messenger' object must be previously created using theIMTServerAPI::MessengerCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The [IMTConMessenger::Name](../../../../Configuration-Interfaces/Messengers/IMTConMessenger/Name.md) value is used for the name.
