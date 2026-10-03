[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [History Data](../History-Data.md) / ChartReplace

[Previous](ChartUpdate.md) | [Next](../Tick-Data.md)

# IMTGatewayAPI::ChartReplace

Full replacement of history data in the specified period with the passed data.

C++
    
    
    MTAPIRES  IMTGatewayAPI::ChartReplace(
       LPCWSTR            symbol,         // Symbol
       const INT64        from,           // Beginning of the period
       const INT64        to,             // End of the period
       const MTChartBar*  bars,           // New bars
       const UINT         bars_total      // Number of new bars
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.ChartReplace(
       string             symbol,         // Number of new bars
       long               from,           // Beginning of the period
       long               to,             // End of the period
       MTChartBar[]       bars            // New bars
       )

### Parameters

**symbol**  
[in] The symbol, for which you want to update historical data.

**from**  
[in] The beginning of the period for which you need to replace data. The date is specified in seconds since January 1, 1970.

**to**  
[in] The date is specified in seconds that have elapsed since 01.01.1970. The date is specified in seconds since January 1, 1970.

**bars**  
[in] New bars, described by theMTChartBarstructure.

**bars_total**  
[in] The number of bars passed.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, a corresponding error code is returned.

### Note

This method totally replaces the history data in the specified time period with the data passed in the 'bars' parameter.
