[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDealSink](../IMTDealSink.md) / OnDealClean

[Previous](OnDealDelete.md) | [Next](OnDealSync.md)

# IMTDealSink::OnDealClean

A handler of the event of clearing of a client's deals.

C++
    
    
    virtual void  IMTDealSink::OnDealClean(
       const UINT64  login       // User's login
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTDealSink.OnDealClean(
       ulong         login       // User's login
       )

### Parameters

**login**  
[in] The login of a user.

### Note

Every day, at server time, expired demo accounts are automatically deleted on trade servers. All deals of these accounts are also deleted. The handler notifies of such an operation and transmits the logins of the accounts whose deals were deleted.
