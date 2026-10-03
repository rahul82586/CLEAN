[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Common Functions](../Common-Functions.md) / LoggerFeederRequest

[Previous](LoggerGatewayRequest.md) | [Next](Release.md)

# IMTAdminAPI::LoggerFeederRequest

Request the logs of [data feeds](../Configuration-Databases/Data-Feeds.md).

C++
    
    
    MTAPIRES  IMTAdminAPI::LoggerFeederRequest(
       const UINT     feeder_pos,        // Position of a data feed
       const INT64    from,              // Start date of the request
       const INT64    to,                // End date of the request
       LPCWSTR        filter,            // Keyword
       MTLogRecord*&  records,           // Array of entries
       UINT&          records_total      // The number of received entries
       )

.NET
    
    
    MTLogRecord[]  CIMTAdminAPI.LoggerFeederRequest(
       uint           feeder_pos,        // Position of a data feed
       long           from,              // Start date of the request
       long           to,                // End date of the request
       string         filter,            // Keyword
       out MTRetCode  res                // Response code
       )

Python
    
    
    AdminAPI.LoggerFeederRequest(
       feeder_pos,    # Position of a data feed
       from,          # Start date of the request
       to,            # End date of the request
       filter         # Keyword
       )

### Parameters

**feeder_pos**  
[in] The position of a data feed in the list of configurations, ranging from 0.

**from**  
[in] The start date for requesting logs. The date is specified in seconds that have elapsed since 01.01.1970.

**to**  
[in] The end date for requesting logs. The date is specified in seconds that have elapsed since 01.01.1970.

**filter**  
[in] A key word for searching logs.

**records**  
[out] A reference to the array of structures that describe logs (MTLogRecord).

**records_total**  
[out] The total number of received journal entries.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

After using, the records array must be released using the [IMTAdminAPI::Free](Free.md) method.
