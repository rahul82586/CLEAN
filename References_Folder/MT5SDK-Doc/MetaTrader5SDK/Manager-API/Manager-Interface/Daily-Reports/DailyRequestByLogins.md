[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Daily Reports](../Daily-Reports.md) / DailyRequestByLogins

[Previous](DailyRequest.md) | [Next](DailyRequestByGroup.md)

# IMTManagerAPI::DailyRequestByLogins

Get an array of daily reports by the list of logins and date range.

C++
    
    
    MTAPIRES  IMTManagerAPI::DailyRequestByLogins(
       const UINT64    logins,       // logins
       const UINT      logins_total, // number of logins
       const INT64     from,         // beginning of period
       const INT64     to,           // end of period
       IMTDailyArray*  daily         // array of report
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.DailyRequestByLogins(
       ulong           logins,       // logins
       long            from,         // beginning of period
       long            to,           // end of period
       CIMTDailyArray  daily         // array of reports
       )

Python
    
    
    ManagerAPI.DailyRequestByLogins(
       logins,         # logins
       from,           # beginning of period
       to              # end of period
       )

### Parameters

**logins**  
[in] Array of client logins.

**logins_total**  
[in] Number of logins in the 'logins' array.

**from**  
[in] The beginning of the period for which you need to get daily reports. The date is specified in seconds since 01.01.1970.

**to**  
[in] The end of the period for which you need to get daily reports. The date is specified in seconds since 01.01.1970.

**daily**  
[out] An object of the array of daily reports. The 'daily' object must be previously created using theIMTManagerAPI::DailyCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies an array of daily reports for the specified logins and date range to the 'daily' object.
