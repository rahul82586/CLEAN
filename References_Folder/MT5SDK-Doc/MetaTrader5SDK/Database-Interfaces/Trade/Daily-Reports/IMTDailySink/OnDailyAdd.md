[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDailySink](../IMTDailySink.md) / OnDailyAdd

[Previous](../IMTDailySink.md) | [Next](OnDailyUpdate.md)

# IMTDailySink::OnDailyAdd

A handler of the event of adding a new daily report.

C++
    
    
    virtual void  IMTDailySink::OnDailyAdd(
       const IMTDaily*  daily      // A pointer to a daily report
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTDailySink.OnDailyAdd(
       CIMTDaily        daily      // A daily report
       )

### Parameters

**daily**  
[in] A pointer to the object of an added daily report.

### Note

This method is used in Server and Report API only.
