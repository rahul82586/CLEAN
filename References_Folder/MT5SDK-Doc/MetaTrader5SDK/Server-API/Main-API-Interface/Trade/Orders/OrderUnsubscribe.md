[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Orders](../Orders.md) / OrderUnsubscribe

[Previous](OrderSubscribe.md) | [Next](OrderAdd.md)

# IMTServerAPI::OrderUnsubscribe

Unsubscribe from the events and hooks associated with changes in the database of open orders.
    
    
    MTAPIRES  IMTServerAPI::OrderUnsubscribe(
       IMTOrderSink*  sink      // A pointer to the IMTOrderSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTOrderSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This is a pair method to [IMTServerAPI::OrderSubscribe](OrderSubscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) error is returned.
