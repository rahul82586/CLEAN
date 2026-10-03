[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Messengers](../Messengers.md) / MessengerUnsubscribe

[Previous](MessengerSubscribe.md) | [Next](MessengerUpdate.md)

# IMTAdminAPI::MessengerUnsubscribe

Unsubscribe from events and hooks associated with messenger configurations.

C++
    
    
    MTAPIRES  IMTAdminAPI::MessengerUnsubscribe(
       IMTConMessengerSink*  sink   // A pointer to the IMTConMessengerSink object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.MessengerUnsubscribe(
       CIMTConMessengerSink  sink      // The CIMTConMessengerSink object
       )

Python
    
    
    AdminAPI.MessengerUnsubscribe(
       sink                  # IMTConMessengerSink object
       )

### Parameters

**sink**  
[in] A pointer to the object which implements theIMTConMessengerSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This is a pair method to [IMTServerAPI::MessengerSubscribe](../../../../Server-API/Main-API-Interface/Configuration-Databases/Messengers/MessengerSubscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) error is returned.
