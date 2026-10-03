[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Deals](../Deals.md) / DealSubscribe

[Previous](DealCreateArray.md) | [Next](DealUnsubscribe.md)

# IMTManagerAPI::DealSubscribe

Subscribe to events associated with changes in the database of deals.

C++
    
    
    MTAPIRES  IMTManagerAPI::DealSubscribe(
       IMTDealSink*  sink      // A pointer to the IMTDealSink object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.DealSubscribe(
       CIMTDealSink  sink      // CIMTDealSink object
       )

Python
    
    
    ManagerAPI.DealSubscribe(
       sink          # IMTDealSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTDealSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Subscribing to events is thread safe. One and the same interface [IMTDealSink](../../../../Database-Interfaces/Trade/Deals/IMTDealSink.md) cannot subscribe to an event twice - in this case the response code [MT_RET_ERR_DUPLICATE](../../../../Return-Codes/Common-errors.md) is returned.
