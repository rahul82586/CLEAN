[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Network](../Network.md) / NetServerUnsubscribe

[Previous](NetServerSubscribe.md) | [Next](NetServerRestart.md)

# IMTAdminAPI::NetServerUnsubscribe

Unsubscribe from events associated with the configuration of the platform components.

C++
    
    
    MTAPIRES  IMTAdminAPI::NetServerUnsubscribe(
       IMTConServerSink*  sink      // A pointer to the IMTConServerSink object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.NetServerUnsubscribe(
       CIMTConServerSink  sink      // CIMTConServerSink object
       )

Python
    
    
    AdminAPI.NetServerUnsubscribe(
       sink      # IMTConServerSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTConServerSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This is a pair method to [IMTAdminAPI::NetServerSubscribe](NetServerSubscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) error is returned.
