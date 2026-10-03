[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Orders](../../Orders.md) / [IMTHistorySink](../IMTHistorySink.md) / OnHistoryUpdate

[Previous](OnHistoryAdd.md) | [Next](OnHistoryDelete.md)

# IMTHistorySink::OnHistoryUpdate

A handler of the event of modifying a closed order.

C++
    
    
    virtual void  IMTHistorySink::OnHistoryUpdate(
       const IMTOrder*  order      // A pointer to the order object
       )

.NET
    
    
    virtual void  ICIMTHistorySink::OnHistoryUpdate(
       CIMTOrder        order      // Order object
       )

### Parameters

**order**  
[in] A pointer to the object of an updated order.

### Note

This method is used in Server API only. It is called to notify of the modification of a closed order.
