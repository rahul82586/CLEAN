[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDailySink](../IMTDailySink.md) / OnDailyDelete

[Previous](OnDailyUpdate.md) | [Next](OnDailyClear.md)

# IMTDailySink::OnDailyDelete

A handler of the event of removing a daily report.

C++
    
    
    virtual void  IMTDailySink::OnDailyDelete(
       const IMTDaily*  daily      // A pointer to a daily report
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTDailySink.OnDailyDelete(
       CIMTDaily        daily      // A daily report
       )

### Parameters

**daily**  
[in] A pointer to the object of a deleted daily report.

### Note

This method is used in Server and Report API only.
