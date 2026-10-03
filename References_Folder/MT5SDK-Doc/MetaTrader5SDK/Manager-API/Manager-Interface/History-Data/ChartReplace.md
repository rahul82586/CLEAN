[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [History Data](../History-Data.md) / ChartReplace

[Previous](ChartUpdate.md) | [Next](ChartSplit.md)

# IMTManagerAPI::ChartReplace

Completely replace historical data in the specified period by the transmitted data

C++
    
    
    MTAPIRES  IMTManagerAPI::ChartReplace(
       LPCWSTR            symbol,         // Symbol
       const INT64        from,           // Beginning of the period
       const INT64        to,             // End of the period
       const MTChartBar*  bars,           // New bars
       const UINT         bars_total      // Number of new bars
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.ChartReplace(
       string             symbol,         // Symbol
       long               from,           // Beginning of the period
       long               to,             // End of the period
       MTChartBar[]       bars            // New bars
       )

Python
    
    
    ManagerAPI.ChartReplace(
       symbol,            # Symbol
       from,              # Beginning of the period
       to,                # End of the period
       bars               # New bars
       )

### Parameters

**symbol**  
[in] The symbol, for which you want to update historical data.

**from**  
[in] The beginning date of the period for which you want to replace data. The date is specified in seconds since 01.01.1970.

**to**  
[in] The end date of the period for which you want to replace data. The date is specified in seconds since 01.01.1970.

**bars**  
[in] New bars described by theMTChartBarstructure.

**bars_total**  
[in] The number of passed bars.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, a corresponding error code is returned.

### Note

The method completely replaces historical data in the specified time interval with the data passed in the 'bars' parameter.
