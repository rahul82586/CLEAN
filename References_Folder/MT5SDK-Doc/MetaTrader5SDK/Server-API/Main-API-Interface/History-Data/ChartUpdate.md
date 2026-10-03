[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [History Data](../History-Data.md) / ChartUpdate

[Previous](ChartDelete.md) | [Next](ChartSplit.md)

# IMTServerAPI::ChartUpdate

Change historical data of a symbol.
    
    
    MTAPIRES  IMTAdminAPI::ChartUpdate(
       LPCWSTR            symbol,         // Symbol
       const MTChartBar*  bars,           // Bars to change
       const UINT         bars_total      // The number of bars to change
       )

### Parameters

**symbol**  
[in] The symbol, for which you want to update historical data.

**bars**  
[in] Bars you want to update, described by theMTChartBarstructure.

**bars_total**  
[in] The number of bars to update.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method can be used only on history servers.
