[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Custom Functions](../Custom-Functions.md) / CustomUnsubscribe

[Previous](CustomSubscribe.md) | [Next](CustomCreateStream.md)

# IMTServerAPI::CustomUnsubscribe

Unsubscribe from events and hooks associated with the execution of custom functions.
    
    
    MTAPIRES  IMTServerAPI::CustomUnsubscribe(
       IMTCustomSink*  sink      // A pointer to the IMTCustomSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTCustomSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This is a pair method to [IMTServerAPI::CustomSubscribe](CustomSubscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) error is returned.
