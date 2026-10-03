[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [History Data](../History-Data.md) / ChartUpdate

[Previous](ChartDelete.md) | [Next](ChartReplace.md)

# IMTAdminAPI::ChartUpdate

Change historical data of a symbol.

C++
    
    
    MTAPIRES  IMTAdminAPI::ChartUpdate(
       LPCWSTR            symbol,         // Symbol
       const MTChartBar*  bars,           // Bars to change
       const UINT         bars_total      // The number of bars to change
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.ChartUpdate(
       string             symbol,         // Number of new bars
       MTChartBar[]       bars            // Bars to change   
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

If the open price of a bar ([MTChartBar.open](../../../Structures/MTChartBar.md)) passed in the structure is 0, the bar will be deleted.
