[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Daily Reports](../Daily-Reports.md) / DailyGetLight

[Previous](DailyGet.md) | [Next](DailySelect.md)

# IMTReportAPI::DailyGetLight

Get the eased version of a daily report.
    
    
    MTAPIRES  IMTReportAPI::DailyGetLight(
       const UINT64  login,        // Client login
       const INT64   datetime,     // Date and time
       IMTDaily      *daily        // An object of a daily report
       )

### Parameters

**login**  
[in] The login of a client.

**datetime**  
[in] Daily report generation date and time. The date is specified in seconds that have elapsed since 01.01.1970. Daily reports for the period can be requested using the IMTReportAPI::DailyGetLight second variant to get a report generation date and time. Then reports generation date and time can be stored and used in the function current variant.

***daily**  
[out] An object of a daily report. The daily object must be first created using theIMTReportAPI::DailyCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method submits all daily report parameters except orders ([IMTDaily::Order*](../../../Database-Interfaces/Trade/Daily-Reports/IMTDaily/OrderAdd.md)) and positions ([IMTDaily::Position*](../../../Database-Interfaces/Trade/Daily-Reports/IMTDaily/PositionAdd.md)).

# IMTReportAPI::DailyGetLight

Get an eased daily reports array.
    
    
    MTAPIRES  IMTReportAPI::DailyGetLight(
       const UINT64   login,      // Client login
       const INT64    from,       // Beginning of period
       const INT64    to,         // End of period
       IMTDailyArray  *daily      // Reports array
       )

### Parameters

**login**  
[in] The login of a client.

**from**  
[in] The beginning of the period for which you need to get daily reports. The date is specified in seconds that have elapsed since 01.01.1970.

**to**  
[in] The end of the period for which you need to get daily reports. The date is specified in seconds that have elapsed since 01.01.1970.

***daily**  
[out] An object of the array of daily reports. The daily object must be first created using theIMTReportAPI::DailyCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method submits all daily report parameters except orders ([IMTDaily::Order*](../../../Database-Interfaces/Trade/Daily-Reports/IMTDaily/OrderAdd.md)) and positions ([IMTDaily::Position*](../../../Database-Interfaces/Trade/Daily-Reports/IMTDaily/PositionAdd.md)).
