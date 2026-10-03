[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Orders](../../Orders.md) / [IMTOrderSink](../IMTOrderSink.md) / OnOrderUpdate

[Previous](OnOrderAdd.md) | [Next](OnOrderDelete.md)

# IMTOrderSink::OnOrderUpdate

A handler of the event of modifying an open order.

C++
    
    
    virtual void  IMTOrderSink::OnOrderUpdate(
       const IMTOrder*  order      // A pointer to the order object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTOrderSink.OnOrderUpdate(
       CIMTOrder        order      // Order object
       )

### Parameters

**order**  
[in] A pointer to the object of an updated order.

### Note

This method is called by the API to notify of the modification of an open order.
