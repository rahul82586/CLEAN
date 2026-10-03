[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Time](../Time.md) / Unsubscribe

[Previous](Subscribe.md) | [Next](Get.md)

# IMTAdminAPI::TimeUnsubscribe

Unsubscribe from events associated with time configuration.

C++
    
    
    MTAPIRES  IMTAdminAPI::TimeUnsubscribe(
       IMTConTimeSink*  sink      // A pointer to the IMTConTimeSink object
       )

.NT
    
    
    MTRetCode  CIMTAdminAPI.TimeUnsubscribe(
       CIMTConTimeSink  sink      // CIMTConTimeSink object
       )

Python
    
    
    AdminAPI.TimeUnsubscribe(
       sink             # IMTConTimeSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTConTimeSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This is a pair method to [IMTAdminAPI::TimeSubscribe](Subscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) error is returned.
