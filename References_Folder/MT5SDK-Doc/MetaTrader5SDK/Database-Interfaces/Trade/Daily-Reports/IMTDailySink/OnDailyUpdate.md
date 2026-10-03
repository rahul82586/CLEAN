[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDailySink](../IMTDailySink.md) / OnDailyUpdate

[Previous](OnDailyAdd.md) | [Next](OnDailyDelete.md)

# IMTDailySink::OnDailyUpdate

A handler of the event of updating a daily report.

C++
    
    
    virtual void  IMTDailySink::OnDailyUpdate(
       const IMTDaily*  daily      // A pointer to a daily report
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTDailySink.OnDailyUpdate(
       CIMTDaily        daily      // A daily report
       )

### Parameters

**daily**  
[in] A pointer to the object of an updated daily report.

### Note

This method is used in Server and Report API only.
