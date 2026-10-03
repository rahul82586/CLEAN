[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Common](../Common.md) / Unsubscribe

[Previous](Subscribe.md) | [Next](Get.md)

# IMTServerAPI::CommonUnsubscribe

Unsubscribe from events and hooks associated with the common configuration of the platform.
    
    
    MTAPIRES  IMTServerAPI::CommonUnsubscribe(
       IMTConCommonSink*  sink      // A pointer to the IMTConCommonSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTConCommonSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This is a pair method to [IMTServerAPI::CommonSubscribe](Subscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) error is returned.
