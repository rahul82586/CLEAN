[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Managers](../Managers.md) / ManagerUnsubscribe

[Previous](ManagerSubscribe.md) | [Next](ManagerUpdate.md)

# IMTAdminAPI::ManagerUnsubscribe

Unsubscribe from events associated with the configuration of managers.

C++
    
    
    MTAPIRES  IMTAdminAPI::ManagerUnsubscribe(
       IMTConManagerSink*  sink      // A pointer to the IMTConManagerSink object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.ManagerUnsubscribe(
       CIMTConManagerSink  sink      // CIMTConManagerSink object
       )

Python
    
    
    AdminAPI.ManagerUnsubscribe(
       sink                # IMTConManagerSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTConManagerSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This is a pair method to [IMTAdminAPI::ManagerSubscribe](ManagerSubscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) error is returned.
