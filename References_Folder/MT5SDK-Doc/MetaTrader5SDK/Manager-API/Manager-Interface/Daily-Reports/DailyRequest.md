[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Daily Reports](../Daily-Reports.md) / DailyRequest

[Previous](DailyCreateArray.md) | [Next](DailyRequestByLogins.md)

# IMTManagerAPI::DailyRequest

Get an array of daily reports by the login and date range.

C++
    
    
    MTAPIRES  IMTManagerAPI::DailyRequest(
       const UINT64    login,     // Login
       const INT64     from,      // Beginning of period
       const INT64     to,        // End of period
       IMTDailyArray*  daily      // Reports array
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.DailyRequest(
       ulong           login,     // Login
       long            from,      // Beginning of period
       long            to,        // End of period
       CIMTDailyArray  daily      // Reports array
       )

Python
    
    
    ManagerAPI.DailyRequest(
       login,          # Login
       from,           # Beginning of period
       to              # End of period
       )

### Parameters

**login**  
[in] The login of the client, whose daily report you need to get.

**from**  
[in] The beginning of the period for which you need to get daily reports. The date is specified in seconds that have elapsed since 01.01.1970.

**to**  
[in] The end of the period for which you need to get daily reports. The date is specified in seconds that have elapsed since 01.01.1970.

**daily**  
[out] An object of the array of daily reports. The daily object must be first created using theIMTManagerAPI::DailyCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

This method copies an array of daily reports by the specified login and date range to the daily object.
