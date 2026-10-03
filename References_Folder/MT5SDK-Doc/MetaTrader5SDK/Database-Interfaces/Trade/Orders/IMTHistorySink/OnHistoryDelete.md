[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Orders](../../Orders.md) / [IMTHistorySink](../IMTHistorySink.md) / OnHistoryDelete

[Previous](OnHistoryUpdate.md) | [Next](OnHistoryClean.md)

# IMTHistorySink::OnHistoryDelete

A handler of the event of deleting a closed order.

C++
    
    
    virtual void  IMTHistorySink::OnHistoryDelete(
       const IMTOrder*  order      // A pointer to the order object
       )

.NET
    
    
    virtual void  CIMTHistorySink.OnHistoryDelete(
       CIMTOrder        order      // Order object
       )

### Parameters

**order**  
[in] A pointer to the object of a deleted order.

### Note

This method is used in Server API only. It is called to notify that a closed order has been deleted.
