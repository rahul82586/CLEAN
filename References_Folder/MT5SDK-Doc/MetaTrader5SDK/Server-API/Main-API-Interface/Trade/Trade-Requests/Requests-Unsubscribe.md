[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Trade Requests](../Requests.md) / Requests Unsubscribe

[Previous](Requests-Subscribe.md) | [Next](Requests-Request.md)

# IMTServerAPI::TradeUnsubscribe

Unsubscribe from events and hooks associated with trade requests.
    
    
    MTAPIRES  IMTServerAPI::TradeUnsubscribe(
       IMTTradeSink*  sink      // A pointer to the IMTTradeSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTTradeSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This is a pair method to [IMTServerAPI::TradeSubscribe](Requests-Subscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) error is returned.
