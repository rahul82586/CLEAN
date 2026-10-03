[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Messengers](../Messengers.md) / MessengerNext

[Previous](MessengerTotal.md) | [Next](MessengerGet.md)

# IMTAdminAPI::MessengerNext

Get a messenger configuration by index.

C++
    
    
    MTAPIRES  IMTAdminAPI::MessengerNext(
       const UINT        pos,       // Configuration position
       IMTConMessenger*  messenger  // Messenger configuration object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.MessengerNext(
       uint              pos,       // Configuration position
       CIMTConMessenger  messenger  // Messenger configuration object
       )

Python
    
    
    AdminAPI.MessengerNext(
       pos               # Configuration position
       )

### Parameters

**pos**  
[in] Position of the configuration, starting with 0.

**messenger**  
[out] Messenger configuration object. The 'messenger' object must be previously created using theIMTAdminAPI::MessengerCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the configuration data of a messenger with a specified index to the 'messenger' object.
