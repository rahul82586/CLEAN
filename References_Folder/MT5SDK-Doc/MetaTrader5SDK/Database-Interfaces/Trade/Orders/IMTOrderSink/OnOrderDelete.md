[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Orders](../../Orders.md) / [IMTOrderSink](../IMTOrderSink.md) / OnOrderDelete

[Previous](OnOrderUpdate.md) | [Next](OnOrderClean.md)

# IMTOrderSink::OnOrderDelete

A handler of the event of deleting an open order.

C++
    
    
    virtual void  IMTOrderSink::OnOrderDelete(
       const IMTOrder*  order      // A pointer to the order object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTOrderSink.OnOrderDelete(
       CIMTOrder        order      // A pointer to the order object
       )

### Parameters

**order**  
[in] A pointer to the object of a deleted order.

### Note

This method is called by the API to notify that an open order has been deleted.
