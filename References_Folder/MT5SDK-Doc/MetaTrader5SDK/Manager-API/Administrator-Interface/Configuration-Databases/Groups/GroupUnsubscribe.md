[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Groups](../Groups.md) / GroupUnsubscribe

[Previous](GroupSubscribe.md) | [Next](GroupUpdate.md)

# IMTAdminAPI::GroupUnsubscribe

Unsubscribe from events associated with the configuration of groups.

C++
    
    
    MTAPIRES  IMTAdminAPI::GroupUnsubscribe(
       IMTConGroupSink*  sink      // A pointer to the IMTConGroupSink object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.GroupUnsubscribe(
       CIMTConGroupSink  sink      // CIMTConGroupSink object
       )

Python
    
    
    AdminAPI.GroupUnsubscribe(
       sink              # IMTConGroupSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTConGroupSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This is a pair method to [IMTAdminAPI::GroupSubscribe](GroupSubscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) error is returned.
