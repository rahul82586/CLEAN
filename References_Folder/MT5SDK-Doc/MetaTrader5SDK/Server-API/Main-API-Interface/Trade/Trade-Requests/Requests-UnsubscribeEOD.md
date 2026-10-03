[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Trade Requests](../Requests.md) / Requests UnsubscribeEOD

[Previous](Requests-SubscribeEOD.md) | [Next](Requests-AccountSet.md)

# IMTServerAPI::TradeUnsubscribeEOD

Unsubscribe from events associated with operations performed at the end of a trading day/month.
    
    
    MTAPIRES  IMTServerAPI::TradeUnsubscribeEOD(
       IMTEndOfDaySink*  sink      // A pointer to the IMTEndOfDaySink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTEndOfDaySinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This is a pair method to [IMTServerAPI::TradeSubscribeEOD](Requests-SubscribeEOD.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) error is returned.
