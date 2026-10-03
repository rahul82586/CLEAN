[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Time](../Time.md) / Unsubscribe

[Previous](Subscribe.md) | [Next](Get.md)

# IMTManagerAPI::TimeUnsubscribe

Unsubscribe from events associated with time configuration.

C++
    
    
    MTAPIRES  IMTManagerAPI::TimeUnsubscribe(
       IMTConTimeSink*  sink      // A pointer to the IMTConTimeSink object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.TimeUnsubscribe(
       CIMTConTimeSink  obj       // CIMTConTimeSink object
       )

Python
    
    
    ManagerAPI.TimeUnsubscribe(
       sink             # IMTConTimeSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTConTimeSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method is pared to [IMTManagerAPI::TimeSubscribe](Subscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) error is returned.
