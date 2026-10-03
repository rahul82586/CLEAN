[🏠 Document Start](../../README.md) / [Server API](../README.md) / [Interface of End-of-Day Events](../Interface-of-End-of-Day-Events.md) / OnEOMGroupStatements

[Previous](OnEOMGroupInterest.md) | [Next](OnEOMGroupFinish.md)

# IMTEndOfDaySink::OnEOMGroupStatements

A handler of the event of start of daily report generation for the specified group at the end of the trading month.
    
    
    virtual void  IMTEndOfDaySink::OnEOMGroupStatements(
       const INT64         datetime,          // Time of the event
       const INT64         prev_datetime,     // Time of the previous event
       const IMTConGroup*  group              // Group
       )

### Parameters

**datetime**  
[out] Time of the event in seconds that elapsed since 01.01.1970.

**prev_datetime**  
[out] Time of the previous similar event in seconds that elapsed since 01.01.1970.

**group**  
[out]The object of the group, with which the event is associated.

### Note

This method notifies of start of adding appropriate records to the database of daily reports and of generation of HTML reports for the clients in the group (in case this [option](../../Configuration-Interfaces/Groups/IMTConGroup/ReportsFlags.md) is enabled).
