[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [History Data](../History-Data.md) / ChartGet

[Previous](ChartUnsubscribe.md) | [Next](ChartDelete.md)

# IMTServerAPI::ChartGet

Request minute bars for a symbol.
    
    
    MTAPIRES  IMTServerAPI::ChartGet(
       LPCWSTR       symbol,         // Symbol
       const INT64   from,           // Beginning of the period
       const INT64   to,             // End of the period
       MTChartBar*&  bars,           // Array of bars
       UINT&         bars_total      // Number of received bars
       )

### Parameters

**symbol**  
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

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method can be used both on the trade and on the history servers.
