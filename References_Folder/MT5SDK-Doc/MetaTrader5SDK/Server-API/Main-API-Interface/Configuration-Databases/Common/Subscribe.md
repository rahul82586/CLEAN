[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Common](../Common.md) / Subscribe

[Previous](CreateAgreement.md) | [Next](Unsubscribe.md)

# IMTServerAPI::CommonSubscribe

Subscribe to events and hooks associated with the common configuration of the platform.
    
    
    MTAPIRES  IMTServerAPI::CommonSubscribe(
       IMTConCommonSink*  sink      // A pointer to the IMTConCommonSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTConCommonSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Subscribing to events is thread safe. One and the same [IMTConCommonSink](../../../../Configuration-Interfaces/Common/IMTConSink.md) interface cannot subscribe to an event twice - in this case the response code [MT_RET_ERR_DUPLICATE](../../../../Return-Codes/Common-errors.md) is returned.
