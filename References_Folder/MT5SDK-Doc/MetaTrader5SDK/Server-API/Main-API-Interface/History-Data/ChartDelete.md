[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [History Data](../History-Data.md) / ChartDelete

[Previous](ChartGet.md) | [Next](ChartUpdate.md)

# IMTServerAPI::ChartDelete

Delete a bar by the symbol.
    
    
    MTAPIRES  IMTServerAPI::ChartDelete(
       LPCWSTR            symbol,         // Symbol
       const INT64*       bars_dates,     // Time of bars to delete
       const UINT         bars_total      // The number of bars to delete
       )

### Parameters

**symbol**  
[in] The symbol, for which you want to delete historical data.

**bars_dates**  
[in] Time of bars you want to delete; specified in the number of seconds elapsed since 01.01.1970.

**bars_total**  
[in] The number of bars to delete.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method can be used only on history servers.
