[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Trade Requests](../Requests.md) / Requests SubscribeEOD

[Previous](Requests-BalanceCheck.md) | [Next](Requests-UnsubscribeEOD.md)

# IMTServerAPI::TradeSubscribeEOD

Subscribe to events associated with operations performed at the end of a trading day/month.
    
    
    MTAPIRES  IMTServerAPI::TradeSubscribeEOD(
       IMTEndOfDaySink*  sink      // A pointer to the IMTEndOfDaySink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTEndOfDaySinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Subscribing to events is thread safe. One and the same interface [IMTEndOfDaySink](../../../Interface-of-End-of-Day-Events.md) cannot subscribe to an event twice - in this case the response code [MT_RET_ERR_DUPLICATE](../../../../Return-Codes/Common-errors.md) is returned.
