[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Orders](../../Orders.md) / [IMTOrderSink](../IMTOrderSink.md) / OnOrderClean

[Previous](OnOrderDelete.md) | [Next](OnOrderSync.md)

# IMTOrderSink::OnOrderClean

A handler of the event of clearing open orders of a client.

C++
    
    
    virtual void  IMTOrderSink::OnOrderClean(
       const UINT64  login      // User's login
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTOrderSink.OnOrderClean(
       ulong         login      // User's login
       )

### Parameters

**login**  
[in] The login of a user.

### Note

Every day, at server time, expired demo accounts are automatically deleted on trade servers. All open orders of these accounts are also deleted. The handler notifies of such an operation and transmits the logins of the accounts whose orders were deleted.
