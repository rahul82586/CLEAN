[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Tick Data](../Tick-Data.md) / TickHistoryReplace

[Previous](TickHistoryAdd.md) | [Next](../Users.md)

# IMTGatewayAPI::TickHistoryReplace

Completely replace tick data in the specified period by the transmitted data

C++
    
    
    MTAPIRES  IMTGatewayAPI::TickHistoryReplace(
       LPCWSTR             symbol,        // Symbol
       const INT64         from_msc,      // Beginning of the period
       const INT64         to_msc,        // End of the period
       const MTTickRate*  ticks,         // New ticks
       const UINT          ticks_total    // Number of new ticks
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.TickHistoryReplace(
       string              symbol,        // Symbol
       long                from_msc,      // Beginning of the period
       long                to_msc,        // End of period
       MTTickRate[]        ticks          // New ticks
       )

### Parameters

**symbol**  
[in] The symbol, for which you want to update tick data.

**from_msc**  
[in] The beginning date of the period for which you want to replace history data. The date is specified in milliseconds since 01.01.1970.

**to_msc**  
[in] The end date of the period for which you want to replace history data. The date is specified in milliseconds since 01.01.1970.

**ticks**  
[in] Array ofMTTickRatestructures, which describe the new ticks.

**ticks_total**  
[in] The number of passed ticks.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method completely replaces tick data in the specified time interval with the data passed in the 'ticks' parameter.
