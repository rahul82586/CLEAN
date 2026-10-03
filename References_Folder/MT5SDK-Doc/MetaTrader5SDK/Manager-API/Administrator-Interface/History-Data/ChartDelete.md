[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [History Data](../History-Data.md) / ChartDelete

[Previous](ChartRequest.md) | [Next](ChartUpdate.md)

# IMTAdminAPI::ChartDelete

Delete a bar by the symbol.

C++
    
    
    MTAPIRES  IMTAdminAPI::ChartDelete(
       LPCWSTR            symbol,           // Symbol
       const INT64*       bars_dates,       // Dates of bars to delete
       const UINT         bars_dates_total  // The number of bars to delete
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.ChartDelete(
       string             symbol,           // Symbol
       long               bars_dates        // Dates of bars to delete
       )

### Parameters

**symbol**  
[in] The symbol, for which you want to delete historical data.

**bars_dates**  
[in] An array of the dates of bars you want to delete. Dates are specified in seconds that have elapsed since 01.01.1970.

**bars_dates_total**  
[in] The number of bars to delete.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
