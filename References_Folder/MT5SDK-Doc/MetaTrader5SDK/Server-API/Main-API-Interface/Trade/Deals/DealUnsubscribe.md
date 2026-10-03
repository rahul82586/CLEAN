[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Deals](../Deals.md) / DealUnsubscribe

[Previous](DealSubscribe.md) | [Next](DealAdd.md)

# IMTServerAPI::DealUnsubscribe

Unsubscribe from the events and hooks associated with changes in the database of deals.
    
    
    MTAPIRES  IMTServerAPI::DealUnsubscribe(
       IMTDealSink*  sink      // A pointer to the IMTDealSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTDealSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This is a pair method to [IMTServerAPI::DealSubscribe](DealSubscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) error is returned.
