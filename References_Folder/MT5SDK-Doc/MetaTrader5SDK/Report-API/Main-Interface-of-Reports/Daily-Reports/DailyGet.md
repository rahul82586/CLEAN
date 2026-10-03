[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Daily Reports](../Daily-Reports.md) / DailyGet

[Previous](DailyCreateArray.md) | [Next](DailyGetLight.md)

# IMTReportAPI::DailyGet

Get a user daily report by date and time.
    
    
    MTAPIRES  IMTReportAPI::DailyGet(
       const UINT64  login,        // Client login
       const INT64   datetime,     // Date and time
       IMTDaily      *daily        // An object of a daily report
       )

### Parameters

**login**  
[in] The login of a client.

**datetime**  
[in] Report generation date and time. The date is specified in seconds that have elapsed since 01.01.1970. Daily reports for the period can be requested using the IMTReportAPI::DailyGet second variant to get a report generation date and time. Then reports generation date and time can be stored and used in the function current variant.

***daily**  
[out] An object of a daily report. The daily object must be first created using theIMTReportAPI::DailyCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

When calling this method Report API limits the end of the request time range by the time of the report generation ([TimeGeneration](../Configuration-Databases/Time/Generation.md)).

# IMTReportAPI::DailyGet

Get an array of daily reports by the date range and login.
    
    
    MTAPIRES  IMTReportAPI::DailyGet(
       const INT64     from,      // Client login
       const INT64     to,        // Beginning of a period
       const UINT64    login,     // End of a period
       IMTDailyArray*  daily      // Reports array
       )

### Parameters

**from**  
[in] The beginning of the period for which you need to get daily reports. The date is specified in seconds that have elapsed since 01.01.1970.

**to**  
[in] The end of the period for which you need to get daily reports. The date is specified in seconds that have elapsed since 01.01.1970.

**login**  
[in] The login of the client, whose daily report you need to get.

**daily**  
[out] An object of the array of daily reports. The daily object must be first created using theIMTReportAPI::DailyCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies an array of daily reports by the specified login and date range to the daily object. When calling this method Report API limits the end of the request time range by the time of the report generation ([IMTReportAPI::TimeGeneration](../Configuration-Databases/Time/Generation.md)).
