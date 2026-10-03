[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Messengers](../Messengers.md) / MessengerGet

[Previous](MessengerNext.md) | [Next](MessengerVerifyPhone.md)

# IMTAdminAPI::MessengerGet

Get a messenger configuration by name.

C++
    
    
    MTAPIRES  IMTAdminAPI::MessengerGet(
       LPCWSTR           name,      // Configuration name
       IMTConMessenger*  messenger  // Messenger configuration object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.MessengerGet(
       string            name,      // Configuration name
       CIMTConMessenger  messenger  // Messenger configuration object
       )

Python
    
    
    AdminAPI.MessengerGet(
       name              # Configuration name
       )

### Parameters

**name**  
[in] The name of the configuration.

**messenger**  
[out] Messenger configuration object. The 'messenger' object must be previously created using theIMTAdminAPI::MessengerCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The [IMTConMessenger::Name](../../../../Configuration-Interfaces/Messengers/IMTConMessenger/Name.md) value is used for the name.
