[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Deals](../Deals.md) / DealUnsubscribe

[Previous](DealSubscribe.md) | [Next](DealRequest.md)

# IMTManagerAPI::DealUnsubscribe

Unsubscribe from the events associated with changes in the database of deals.

C++
    
    
    MTAPIRES  IMTManagerAPI::DealUnsubscribe(
       IMTDealSink*  sink      // A pointer to the IMTDealSink object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.DealUnsubscribe(
       CIMTDealSink  sink      // CIMTDealSink object
       )

Python
    
    
    ManagerAPI.DealUnsubscribe(
       sink          # IMTDealSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTDealSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This is a pair method to [IMTManagerAPI::DealSubscribe](DealSubscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) error is returned.
