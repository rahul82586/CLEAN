[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Daily Reports](../Daily-Reports.md) / DailyRequestByGroup

[Previous](DailyRequestByLogins.md) | [Next](DailyRequestLight.md)

# IMTManagerAPI::DailyRequestByGroup

Get an array of daily reports by groups and date range.

C++
    
    
    MTAPIRES  IMTManagerAPI::DailyRequestByGroup(
       LPCWSTR         group,     // group
       const INT64     from,      // beginning of period
       const INT64     to,        // end of period
       IMTDailyArray*  daily      // array of reports
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.DailyRequestByGroup(
       string          group,     // group
       long            from,      // beginning of period
       long            to,        // end of period
       CIMTDailyArray  daily      // array of reports
       )

Python
    
    
    ManagerAPI.DailyRequestByGroup(
       group,          # group
       from,           # beginning of period
       to              # end of period
       )

### Parameters

**group**  
[in] Groups for which the reports are requested. You can specify one group, several groups (comma separated) or a group mask. The mask is specified using characters "*" (any value) and "!" (exception). For example: "demo*,!demoforex" - all groups whose names begin with 'demo', except for the group demoforex.

**from**  
[in] The beginning of the period for which you need to get daily reports. The date is specified in seconds since 01.01.1970.

**to**  
[in] The end of the period for which you need to get daily reports. The date is specified in seconds since 01.01.1970.

**daily**  
[out] An object of the array of daily reports. The 'daily' object must be previously created using theIMTManagerAPI::DailyCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies an array of daily reports for the specified groups and date range to the 'daily 'object.
