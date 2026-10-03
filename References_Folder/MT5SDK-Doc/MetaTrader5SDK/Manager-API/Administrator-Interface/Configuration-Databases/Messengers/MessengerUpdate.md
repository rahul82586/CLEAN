[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Messengers](../Messengers.md) / MessengerUpdate

[Previous](MessengerUnsubscribe.md) | [Next](MessengerUpdateBatch.md)

# IMTAdminAPI::MessengerAdd

Add or update a messenger configuration.

C++
    
    
    MTAPIRES  IMTAdminAPI::MessengerAdd(
       IMTConMessenger*  config  // Messenger configuration object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.MessengerUpdate(
       CIMTConMessenger  config  // Messenger configuration object
       )

Python
    
    
    AdminAPI.MessengerUpdate(
       config            # Messenger configuration object
       )

### Parameters

**config**  
[in] Messenger configuration object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

A configuration can only be added or updated from the applications running on the main server. For all other plugins the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) will be returned.
