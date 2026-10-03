[🏠 Document Start](../../../../README.md) / [Gateway API](../../../README.md) / [Main Interface](../../../Main-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Common](../Common.md) / Subscribe

[Previous](Create.md) | [Next](Unsubscribe.md)

# IMTGatewayAPI::CommonSubscribe

Subscribe to events associated with the common configuration of the platform.

C++
    
    
    MTAPIRES  IMTGatewayAPI::CommonSubscribe(
       IMTConCommonSink*  sink      // Pointer to the IMTConCommonSink object
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.CommonSubscribe(
       CIMTConCommonSink  sink      // CIMTConCommonSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTConCommonSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Subscribing to events is thread safe. One and the same [IMTConCommonSink](../../../../Configuration-Interfaces/Common/IMTConSink.md) interface cannot subscribe to an event twice. The [MT_RET_ERR_DUPLICATE](../../../../Return-Codes/Common-errors.md) response code is returned in this case.
