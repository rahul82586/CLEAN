[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Daily Reports](../Daily-Reports.md) / DailyGet

[Previous](DailyUnsubscribe.md) | [Next](DailyGetLight.md)

# IMTServerAPI::DailyGet

Get an array of daily reports by the date range and login.
    
    
    MTAPIRES  IMTServerAPI::DailyGet(
       const INT64     from,      // Beginning of period
       const INT64     to,        // End of period
       const UINT64    login,     // Login
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
[out] An object of the array of daily reports. The daily object must be first created using theIMTServerAPI::DailyCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies an array of daily reports by the specified login and date range to the daily object.
