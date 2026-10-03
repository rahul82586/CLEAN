[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Common Functions](../Common-Functions.md) / LoggerGatewayRequest

[Previous](LoggerServerRequest.md) | [Next](LoggerFeederRequest.md)

# IMTAdminAPI::LoggerGatewayRequest

Request the journal of [gateways](../Configuration-Databases/Gateways.md).

C++
    
    
    MTAPIRES  IMTAdminAPI::LoggerGatewayRequest(
       const UINT     gateway_pos,       // Position of a gateway
       const INT64    from,              // Start date of the request
       const INT64    to,                // End date of the request
       LPCWSTR        filter,            // Keyword
       MTLogRecord*&  records,           // Array of entries
       UINT&          records_total      // The number of received entries
       )

.NET
    
    
    MTLogRecord[]  CIMTAdminAPI.LoggerGatewayRequest(
       uint           gateway_pos,       // Position of a gateway
       long           from,              // Start date of the request
       long           to,                // End date of the request
       string         filter,            // Keyword
       out MTRetCode  res                // Array of entries
       )

Python
    
    
    AdminAPI.LoggerGatewayRequest(
       feeder_pos,    # Position of a gateway
       from,          # Start date of the request
       to,            # End date of the request
       filter         # Keyword
       )

### Parameters

**gateway_pos**  
[in] The gateway position in the list of configurations, ranging from 0.

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
