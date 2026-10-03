[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Orders](../Orders.md) / OrderSubscribe

[Previous](OrderCreateArray.md) | [Next](OrderUnsubscribe.md)

# IMTManagerAPI::OrderSubscribe

Subscribe to the events associated with changes in the database of orders.

C++
    
    
    MTAPIRES  IMTManagerAPI::OrderSubscribe(
       IMTOrderSink*  sink      // A pointer to the IMTOrderSink object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.OrderSubscribe(
       CIMTOrderSink  sink      // CIMTOrderSink object
       )

Python
    
    
    ManagerAPI.OrderSubscribe(
       sink           # IMTOrderSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTOrderSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Subscribing to events is thread safe. One and the same interface [IMTOrderSink](../../../../Database-Interfaces/Trade/Orders/IMTOrderSink.md) cannot subscribe to an event twice - in this case the response code [MT_RET_ERR_DUPLICATE](../../../../Return-Codes/Common-errors.md) is returned.
