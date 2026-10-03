[🏠 Document Start](../../../../README.md) / [Gateway API](../../../README.md) / [Main Interface](../../../Main-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Common](../Common.md) / Unsubscribe

[Previous](Subscribe.md) | [Next](Get.md)

# IMTGatewayAPI::CommonUnsubscribe

Unsubscribe from events associated with the common configuration of the platform.

C++
    
    
    MTAPIRES  IMTGatewayAPI::CommonUnsubscribe(
       IMTConCommonSink*  sink      // Pointer to the IMTConCommonSink object
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.CommonUnsubscribe(
       CIMTConCommonSink  sink      // CIMTConCommonSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTConCommonSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This is a pair method to [IMTGatewayAPI::CommonSubscribe](Subscribe.md). If an attempt is made to unsubscribe from the interface which has not been previously subscribed, the [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) error is returned.

The method is not available for data feeds.
