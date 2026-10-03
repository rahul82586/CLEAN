[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Orders](../../Orders.md) / [IMTHistorySink](../IMTHistorySink.md) / OnHistoryAdd

[Previous](../IMTHistorySink.md) | [Next](OnHistoryUpdate.md)

# IMTHistorySink::OnHistoryAdd

A handler of the event of adding a closed order.

C++
    
    
    virtual void  IMTHistorySink::OnHistoryAdd(
       const IMTOrder*  order      // A pointer to the order object
       )

.NET
    
    
    virtual void  CIMTHistorySink.OnHistoryAdd(
       CIMTOrder        order      // Order object
       )

### Parameters

**order**  
[in] A pointer to the object of an added order.

### Note

This method is used in Server API only. It is called to notify of adding of a new closed order.
