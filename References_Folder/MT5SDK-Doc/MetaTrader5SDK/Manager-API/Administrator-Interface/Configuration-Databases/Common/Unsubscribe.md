[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Common](../Common.md) / Unsubscribe

[Previous](Subscribe.md) | [Next](Get.md)

# IMTAdminAPI::CommonUnsubscribe

Unsubscribe from events associated with the common configuration of the platform.

C++
    
    
    MTAPIRES  IMTAdminAPI::CommonUnsubscribe(
       IMTConCommonSink*  sink      // A pointer to the IMTConCommonSink object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.CommonUnsubscribe(
       CIMTConCommonSink  sink      // CIMTConCommonSink object
       )

Python
    
    
    AdminAPI.CommonUnsubscribe(
       sink      # IMTConCommonSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTConCommonSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This is a pair method to [IMTAdminAPI::CommonSubscribe](Subscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) error is returned.
