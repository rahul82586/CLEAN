[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [KYC](../KYC.md) / Subscribe

[Previous](GroupCreate.md) | [Next](Unsubscribe.md)

# IMTAdminAPI::KYCSubscribe

Subscribe to events and hooks associated with KYC provider configurations.

C++
    
    
    MTAPIRES  IMTAdminAPI::KYCSubscribe(
       IMTConKYCSink*  sink   // A pointer to the IMTConKYCSink object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.KYCSubscribe(
       CIMTConKYCSink  sink   // The IMTConKYCSink object
       )

### Parameters

**sink**  
[in] A pointer to the object implementing theIMTConKYCSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error corresponding to the response code has occurred.

### Note

Subscribing to events is thread safe. The same [IMTConKYCSink](../../../../Configuration-Interfaces/KYC/IMTConSink.md) interface cannot be subscribed to an event twice. In this case code [MT_RET_ERR_DUPLICATE](../../../../Return-Codes/Common-errors.md) will be returned.
