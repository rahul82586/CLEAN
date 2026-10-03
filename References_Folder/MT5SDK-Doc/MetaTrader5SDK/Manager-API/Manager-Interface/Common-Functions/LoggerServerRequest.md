[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Common Functions](../Common-Functions.md) / LoggerServerRequest

[Previous](LoggerFlush.md) | [Next](Release.md)

# IMTManagerAPI::LoggerServerRequest

Request the journal of a trade server to which an application is connected.

C++
    
    
    MTAPIRES   IMTManagerAPI::LoggerServerRequest(
       const UINT          mode,         // Request mode
       const UINT          type,         // Event type
       const INT64         from,         // Start date
       const INT64         to,           // End date
       LPCWSTR             filter,       // Keyword
       MTLogRecord*&       records,      // Array of entries
       UINT&               records_total // The number of received entries
       )

.NET
    
    
    MTLogRecord[] CIMTManagerAPI.LoggerServerRequest(
       EnMTLogRequestMode  mode,         // Request mode
       EnMTLogType         type,         // Event type
       long                from,         // Start date
       long                to,           // End date
       string              filter,       // Keyword
       out MTRetCode       res           // Response code
       )

Python
    
    
    ManagerAPI.LoggerServerRequest(
       mode,               # Request mode
       type,               # Event type
       from,               # Start date
       to,                 # End date
       filter              # Keyword
       )

### Parameters

**mode**  
[in] The mode of journal requesting. To pass the mode, theEnMTLogRequestModeenumeration is used.

**type**  
[in] Type of events that should be requested from the server journal. To pass the type of events, theEnMTLogTypeenumeration is used.

**from**  
[in] The start date for requesting logs. The date is specified in seconds that have elapsed since 01.01.1970. Only the date is taken into account, while the exact time is ignored.

**to**  
[in] The end date for requesting logs. The date is specified in seconds that have elapsed since 01.01.1970. Only the date is taken into account, while the exact time is ignored.

**filter**  
[in] Akey wordfor searching logs.

**records**  
[out] A reference to the array of structures that describe logs (MTLogRecord).

**records_total**  
[out] The total number of received journal entries.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, a corresponding error code will be returned.

### Note

After using, the records array must be released using the [IMTManagerAPI::Free](Free.md) method.
