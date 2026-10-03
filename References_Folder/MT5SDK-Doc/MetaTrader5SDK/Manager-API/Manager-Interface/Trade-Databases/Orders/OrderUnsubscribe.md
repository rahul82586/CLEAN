[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Orders](../Orders.md) / OrderUnsubscribe

[Previous](OrderSubscribe.md) | [Next](OrderGet.md)

# IMTManagerAPI::OrderUnsubscribe

Unsubscribe from the events associated with changes in the database of orders.

C++
    
    
    MTAPIRES  IMTManagerAPI::OrderUnsubscribe(
       IMTOrderSink*  sink      // A pointer to the IMTOrderSink object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.OrderUnsubscribe(
       CIMTOrderSink  sink      // CIMTOrderSink object
       )

Python
    
    
    TManagerAPI.OrderUnsubscribe(
       sink           # IMTOrderSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTOrderSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This is a pair method to [IMTManagerAPI::OrderSubscribe](OrderSubscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) error is returned.
