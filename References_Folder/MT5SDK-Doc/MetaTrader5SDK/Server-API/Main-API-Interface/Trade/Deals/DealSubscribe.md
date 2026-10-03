[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Deals](../Deals.md) / DealSubscribe

[Previous](DealCreateArray.md) | [Next](DealUnsubscribe.md)

# IMTServerAPI::DealSubscribe

Subscribe to events and hooks associated with changes in the database of deals.
    
    
    MTAPIRES  IMTServerAPI::DealSubscribe(
       IMTDealSink*  sink      // A pointer to the IMTDealSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTDealSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Subscribing to events is thread safe. One and the same interface [IMTDealSink](../../../../Database-Interfaces/Trade/Deals/IMTDealSink.md) cannot subscribe to an event twice - in this case the response code [MT_RET_ERR_DUPLICATE](../../../../Return-Codes/Common-errors.md) is returned.
