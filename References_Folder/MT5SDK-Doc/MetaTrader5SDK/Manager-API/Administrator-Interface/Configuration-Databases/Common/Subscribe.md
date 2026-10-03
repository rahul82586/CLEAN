[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Common](../Common.md) / Subscribe

[Previous](CreateAgreement.md) | [Next](Unsubscribe.md)

# IMTAdminAPI::CommonSubscribe

Subscribe to events associated with the common configuration of the platform.

C++
    
    
    MTAPIRES  IMTAdminAPI::CommonSubscribe(
       IMTConCommonSink*  sink      // A pointer to the IMTConCommonSink object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.CommonSubscribe(
       CIMTConCommonSink  sink      // CIMTConCommonSink object
       )

Python
    
    
    AdminAPI.CommonSubscribe(
       sink      # IMTConCommonSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTConCommonSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Subscribing to events is thread safe. One and the same [IMTConCommonSink](../../../../Configuration-Interfaces/Common/IMTConSink.md) interface cannot subscribe to an event twice - in this case the response code [MT_RET_ERR_DUPLICATE](../../../../Return-Codes/Common-errors.md) is returned.
