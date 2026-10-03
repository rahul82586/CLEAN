[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Orders](../../Orders.md) / [IMTHistorySink](../IMTHistorySink.md) / OnHistoryClean

[Previous](OnHistoryDelete.md) | [Next](OnHistorySync.md)

# IMTHistorySink::OnHistoryClean

A handler of the event of clearing closed orders of a client.

C++
    
    
    virtual void  IMTHistorySink::OnHistoryClean(
       const UINT64  login      // User's login
       )

.NET
    
    
    virtual void  CIMTHistorySink.OnHistoryClean(
       ulong         login      // User's login
       )

### Parameters

**login**  
[in] The login of a user.

### Note

This method is used in Server API only.
