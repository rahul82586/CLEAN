[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDailySink](../IMTDailySink.md) / OnDailyClear

[Previous](OnDailyDelete.md) | [Next](OnDailySync.md)

# IMTDailySink::OnDailyClean

A handler of the event of clearing of a client's daily reports.

C++
    
    
    virtual void  IMTDailySink::OnDailyClean(
       const UINT64  login      // User's login
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTDailySink.OnDailyClean(
       ulong         login      // User's login
       )

### Parameters

**login**  
[in] The login of a user.

### Note

Every day, at server time, expired demo accounts are automatically deleted on trade servers. All daily reports of these accounts are also deleted. The handler notifies of such an operation and transmits the logins of the accounts whose daily reports were deleted.
