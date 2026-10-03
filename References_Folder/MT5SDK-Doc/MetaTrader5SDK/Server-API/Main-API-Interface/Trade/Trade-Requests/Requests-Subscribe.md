[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Trade Requests](../Requests.md) / Requests Subscribe

[Previous](Requests-ExecutionCreate.md) | [Next](Requests-Unsubscribe.md)

# IMTServerAPI::TradeSubscribe

Subscribe to events and hooks associated with trade requests.
    
    
    MTAPIRES  IMTServerAPI::TradeSubscribe(
       IMTTradeSink*  sink      // A pointer to the IMTTradeSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTTradeSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Subscribing to events is thread safe. One and the same interface [IMTTradeSink](../../../Interface-of-Trade-Events.md) cannot subscribe to an event twice - in this case the response code [MT_RET_ERR_DUPLICATE](../../../../Return-Codes/Common-errors.md) is returned.
