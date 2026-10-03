[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Orders](../../Orders.md) / [IMTHistorySink](../IMTHistorySink.md) / OnHistorySync

[Previous](OnHistoryClean.md) | [Next](../../Deals.md)

# IMTHistorySink::OnHistorySync

A handler of the event of synchronization of a database of closed orders.

C++
    
    
    virtual void  IMTHistorySink::OnHistorySync()

.NET
    
    
    virtual void  CIMTHistorySink.OnHistorySync()

### Note

This method is called only on the trade server in the Server API. It notifies that the synchronization of the database of closed orders between the trade server and its backup server has completed.
