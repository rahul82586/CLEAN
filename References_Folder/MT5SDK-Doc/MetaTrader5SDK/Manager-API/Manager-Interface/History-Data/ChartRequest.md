[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [History Data](../History-Data.md) / ChartRequest

[Previous](../History-Data.md) | [Next](ChartDelete.md)

# IMTManagerAPI::ChartRequest

Request minute bars for a symbol.

C++
    
    
    MTAPIRES  IMTManagerAPI::ChartRequest(
       LPCWSTR       symbol,         // Symbol
       const INT64   from,           // Beginning of the period
       const INT64   to,             // End of the period
       MTChartBar*&  bars,           // Array of bars
       UINT&         bars_total      // Number of received bars
       )

.NET
    
    
    MTChartBar[]  CIMTManagerAPI.ChartRequest(
       string        symbol,         // Symbol
       long          from,           // Beginning of the period
       long          to,             // End of the period
       MTRetCode     res             // Response code
       )

Python
    
    
    ManagerAPI.ChartRequest(
       symbol,       # Symbol
       from,         # Beginning of the period
       to            # End of the period
       )

### Parameters

**news**  
[in] The symbol for which you want to request historical data (bars).

**from**  
[in] The beginning of the period for which you need to get data. The date is specified in seconds that have elapsed since 01.01.1970.

**to**  
[in] The end of the period for which you need to get data. The date is specified in seconds that have elapsed since 01.01.1970.

**bars**  
[out] An array of bars (MTChartBarstructures).

**bars_total**  
[out] The number of obtained bars.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, a corresponding error code will be returned.

### Note

Price data on a History server is stored as 1-minute bars. Higher timeframes are created on the client side, based on the 1-minute bars according to the general principle: bars are used from the first to the last second of the period. For example, the one-hour bar for 13:00 consists of 1-minute bars from 13:00:00 to 13:59:59.
