[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Custom Functions](../Custom-Functions.md) / CustomSubscribe

[Previous](../Custom-Functions.md) | [Next](CustomUnsubscribe.md)

# IMTServerAPI::CustomSubscribe

Subscribe to events and hooks associated with the execution of custom functions.
    
    
    MTAPIRES  IMTServerAPI::CustomSubscribe(
       IMTCustomSink*  sink      // A pointer to the IMTCustomSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTCustomSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Subscribing to events is thread safe. One and the same [IMTCustomSink](../../Interface-of-Custom-Events.md) interface cannot subscribe to an event twice - in this case the response code [MT_RET_ERR_DUPLICATE](../../../Return-Codes/Common-errors.md) is returned.
