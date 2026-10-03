[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Spreads](../Spreads.md) / SpreadSubscribe

[Previous](SpreadLegCreate.md) | [Next](SpreadUnsubscribe.md)

# IMTServerAPI::SpreadSubscribe

Subscribe to events and hooks associated with the configuration of spreads.
    
    
    MTAPIRES  IMTServerAPI::SpreadSubscribe(
       IMTConSpreadSink*  sink      // pointer to IMTConSpreadSink object
       )

### Parameters

**sink**  
[in] Pointer to the object that implementsIMTConSpreadSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Subscribing to events is thread safe. One and the same [IMTConSpreadSink](../../../../Configuration-Interfaces/Spreads/IMTConSpreadSink.md) interface cannot subscribe to an event twice - in this case, [MT_RET_ERR_DUPLICATE](../../../../Return-Codes/Common-errors.md) response code is returned.
