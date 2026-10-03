[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Orders](../../Orders.md) / [IMTOrderSink](../IMTOrderSink.md) / OnOrderAdd

[Previous](../IMTOrderSink.md) | [Next](OnOrderUpdate.md)

# IMTOrderSink::OnOrderAdd

A handler of the event of adding an open order.

C++
    
    
    virtual void  IMTOrderSink::OnOrderAdd(
       const IMTOrder*  order      // A pointer to the order object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTOrderSink.OnOrderAdd(
       CIMTOrder        order      // Order object
       )

### Parameters

**order**  
[in] A pointer to the object of an added order.

### Note

This method is called by the API to notify of adding of a new open order.
